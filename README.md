# grpc_sample
A simple example using grpc with protobuffer 2 in python.
Make sure to have grpc and protobuffer configured in your system.

grpc github repository is [here] (https://github.com/grpc/grpc).

# Build:
Please do all of the following in python2.7 virtual env with proto2.

Cd to the directory grpc_sample before doing following command.

``protoc --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` debate.proto``
``protoc --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` consultation.proto``

`pip install re` #install the regular expression module


# Run:

1 . run with `./start_debate.sh <answer|elaborate> "question" <[timeout]|[blah_run]>`

OR:

2 . run with `python debate_server.py` in one terminal window

   open another terminal window

   run `python debate_client.py <answer|elaborate> "question" <[timeout]|[blah_run]>`


where:

    <answer|elaborate> should be either answer or elaborate with out quote

    "question" should be your question with quote

    <[timeout]|[blah_run]> should be either a number representing timeout, or several numbers representing numbers for blah

    [blah_run] can be left empty


Note:
    I tested the 1st running method on Mac OS X and it works. It is possible that it does not work on other systems.
    If the 1st running method does not work, try the 2nd where run server and client separately.
