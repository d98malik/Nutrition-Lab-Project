
#Api key = AIzaSyAmvrJcT_FRRAFJpl2ZuYO8cr8ATCmDKvQ
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyAmvrJcT_FRRAFJpl2ZuYO8cr8ATCmDKvQ"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

food = "burger"

def analyzer(food):
    food = food.capitalize()
    response = model.generate_content(f"is {food} a type of food? if yes give response as 1 else give response as 0")
    if response.text == "0":
        return f"{food} can not be mapped to any popular food, kindly rephrase and try again."
    else:
        one_serve_size = model.generate_content(f"what is the one serve size of {food} in grams? Reponse with just the number") 
        calories_per_serving = model.generate_content(f"what is the number of calories per serving of {food}? Reponse with just the number")
        return f"One serve size of {food} is {one_serve_size.text} grams. {food} has {calories_per_serving.text} calories per serving."




