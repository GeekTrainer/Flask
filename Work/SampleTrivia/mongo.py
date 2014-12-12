from pymongo import MongoClient;

def CreateTriviaQuestions():
    collection = getCollection();

    questions = [];
    
    question0 = {
        'id': 0,
        'question': 'What year was the Battle of Hastings?',
        'answer': '1066',
    };
    questions.append(question0);

    question1 = {
        'id': 1,
        'question': 'In what country did the Battle of Hastings take place?',
        'answer': 'England',
    };
    questions.append(question1);

    questionsDoc = {
        'title': 'Trivia',
        'questions': questions,
    };

    collection.insert(questionsDoc);

    return;

def GetQuestionsDoc():
    collection = getCollection();
    return collection.find_one();

def getCollection():
    client = MongoClient('mongodb://PythonFlaskMongo:TxrbWR1nYzW_kS_TlaWL43Y0x7JHxHrWDgIsAyMMub8-@ds045097.mongolab.com:45097/PythonFlaskMongo');
    database = client['PythonFlaskMongo'];
    collection = database['Questions'];

    return collection;