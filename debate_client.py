__author__ = 'elaine'

import grpc
from grpc.beta import implementations
import debate_pb2
import sys

def run_client():
    params = sys.argv
    how = params[1]
    question = params[2]
    try:
        channel = implementations.insecure_channel('localhost', 29999)
        stub = debate_pb2.beta_create_Candidate_stub(channel)

        if how.lower() == "answer":
            timeout = int(params[3])
            reply = stub.Answer(debate_pb2.AnswerRequest(question=question, timeout=timeout), timeout+10)

        elif how.lower() == "elaborate":
            blah = params[3:len(sys.argv)]
            for i in range(0, len(blah)):
                blah[i] = int(blah[i])
            reply = stub.Elaborate(debate_pb2.ElaborateRequest(topic=question, blah_run=blah), 10)

        print reply.answer

    except grpc.framework.interfaces.face.face.ExpirationError:
        print "No comment"

if __name__ == "__main__":
    run_client()