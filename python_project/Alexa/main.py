import json
import wikipedia
from  difflib import  get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path,'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str,data: dict):
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)


def find_best_match(user_question: str,questions: list[str]) -> str | None:
    matches: list  = get_close_matches(user_question,questions , n=1 , cutoff=0.9)
    return matches[0] if matches else None




def get_answer_for_question(question: str,knowledge_base: dict) -> str | None :
    for q in knowledge_base["questions"]:
       if q["question"] == question:
          return q["answer"]



def chat():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You:')
        if user_input.lower()=='quit':
            break;

        best_match:str | None = find_best_match(user_input,[q["question"]for q in knowledge_base["questions"]])




        if 'search on wikipedia' in user_input:
            name= user_input.replace('search on wikipedia','')
            new_answer = wikipedia.summary(name, sentences=3)
            print(new_answer)
            if new_answer.lower() != 'sp':
                best_match: str | None = find_best_match(name,
                                                         [q["question"] for q in knowledge_base["questions"]])
                if best_match:
                    print("")
                else:
                    knowledge_base["questions"].append({"question":name,"answer" : new_answer})
                    save_knowledge_base('knowledge_base.json',knowledge_base)
        elif best_match:
            answer: str = get_answer_for_question(best_match,knowledge_base)
            print(f'Bot:{answer}')


        else:
            print(('Bot: I don\'t know the answer . Can you teach me ? '))
            new_answer: str = input('Type the answer or "sp"  to skip :')


            if new_answer.lower() != 'sp':
                knowledge_base["questions"].append({"question":user_input,"answer" : new_answer})
                save_knowledge_base('knowledge_base.json',knowledge_base)
                print('Bot : Thank You ! I learned a new response!')





if __name__ == '__main__':
    chat()
