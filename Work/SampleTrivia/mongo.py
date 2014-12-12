from pymongo import MongoClient;

def CreateTriviaQuestions():
    collection = getCollection();

    question0 = {
        'questionID': 0,
        'text': 'What year was the Battle of Hastings?',
        'answer': '1066',
    };
    collection.insert(question0);

    question1 = {
        'questionID': 1,
        'text': 'In what country did the Battle of Hastings take place?',
        'answer': 'England',
    };

    collection.insert(question1);

    return;

def GetQuestions():
    collection = getCollection();
    return collection.find();

def GetQuestion(questionID):
    collection = getCollection();
    return collection.find_one({'questionID':questionID});

def getCollection():
    client = MongoClient('mongodb://PythonFlaskMongo:TxrbWR1nYzW_kS_TlaWL43Y0x7JHxHrWDgIsAyMMub8-@ds045097.mongolab.com:45097/PythonFlaskMongo');
    database = client['PythonFlaskMongo'];
    collection = database['Questions'];

    return collection;