__author__ = 'elaine'

import debate_pb2
import consultation_pb2
import re
import random
import grpc
from grpc.beta import implementations

class Debate(debate_pb2.BetaCandidateServicer):

    def Answer(self, request, context=None):
        if re.match("^(why|what|how|who|when)", request.question, re.IGNORECASE):
            replaced = re.sub("your", "my", request.question, len(request.question), re.IGNORECASE)
            replaced = re.sub("you", "I", replaced, len(request.question), re.IGNORECASE)

            try:
                channel = implementations.insecure_channel('54.88.18.92', 50051)
                stub = consultation_pb2.beta_create_CampaignManager_stub(channel)
                response = stub.Retort(consultation_pb2.RetortRequest(original_question=replaced), request.timeout+10)
                ans = 'You asked me %s but I want to say that %s.' % (replaced, response.retort)

            except grpc.framework.interfaces.face.face.ExpirationError:
                ans = 'No comment.'

        else:
            i = random.randint(0, 1)
            if i == 0:
                ans = 'Your 3 cent titanium tax goes too far.'
            else:
                ans = 'Your 3 cent titanium tax doesn\'t go too far enough.'

        return debate_pb2.AnswerReply(answer=ans)

    def Elaborate(self, request, context=None):
        sentence = request.topic
        num = request.blah_run
        ret_mes = ""
        if len(num) == 0:
            ret_mes = sentence
        elif len(num) == 1:
            ret_mes = "blah "*num[0] + sentence
        else:
            for i in range(0, len(num)-1):
                ret_mes += "blah " * num[i] + sentence
            ret_mes += "blah "* num[-1]
        return debate_pb2.ElaborateReply(answer=ret_mes)

def run_server():
    server = debate_pb2.beta_create_Candidate_server(Debate())
    server.add_insecure_port('localhost:29999')
    server.start()

if __name__ == "__main__":
    run_server()
