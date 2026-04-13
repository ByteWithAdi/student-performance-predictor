import pickle

model = pickle.load(open('../model/model.pkl', 'rb'))

def predict_student(hours, sleep, attendance, marks):
    result = model.predict([[hours, sleep, attendance, marks]])
    return "Pass" if result[0] == 1 else "Fail"