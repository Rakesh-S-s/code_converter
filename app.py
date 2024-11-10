from flask import Flask, render_template,request, jsonify
import google.generativeai as genai
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('API_KEY'))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

app = Flask(__name__)

code_data = ""
uploaded_code_content=""
selected_language = ""
converted_code=""
selected_language0=""
file_path=""

language_list={"python": "demopy.py","java":"main.java","c#":"democsharp.cs","c++":"democpp.cpp","c":"democ.c","cobol":"democobol.cob","javascript":"demojs.js"}

compiler_list={"python":"compiler_python.py","java":"compiler_java.py","c#":"compiler_csharp.py","c++":"compiler_cpp.py","c":"compiler_c.py","cobol":"compile_cobol.py"}

converter_code_file={"python":"converted_py.py","java":"converted_java.java","c#":"converted_cs.cs","c++":"converted_cpp.cpp","c":"converted_c.c","cobol":"converted_cobol.cob","javascript":"convert_js.js"}


@app.route('/')
def index():
    return render_template('index.html')

# Route for 'Code Analyzer' button
@app.route('/analyze')
def analyze():
    return render_template('index1.html')

# Route for 'Code Converter' button
@app.route('/converter')
def convert():
    print(code_data)
    return render_template('index2.html')

#stores the language of the input code file
@app.route('/save_selected_language', methods=['POST'])
def save_selected_language():
    global selected_language0
    data = request.get_json()
    selected_language0 = data.get('language')
    with open("code_lang.txt", 'w') as file:
        file.write(selected_language0)
    print("Selected language:", selected_language0)
    return jsonify({"success": True, "selected_language": selected_language0})

#route recieves the uploaded code and calls the function to store it in corresponding extension file - COmpleted Fully
@app.route('/store_code', methods=['POST'])
def store_code():
    global uploaded_code_content
    data = request.get_json()
    uploaded_code_content = data.get('content', '')
    code_data = data.get('content')
    # print(uploaded_code_content)
    if uploaded_code_content:
        print("Content received and stored successfully.")
        store_file0(uploaded_code_content)
        return jsonify({"success": True})
    else:
        print("Failed to store content.")
        return jsonify({"success": False}), 400

#uploads the input coding file into corresponding extension file - fully completed
def store_file0(uploaded_code_content):
    # print("hey bro")
    language=""
    with open('code_lang.txt', 'r') as file:
        language = file.read()
    global file_path
    file_path=language_list[f"{language}"]
    # print(file_path)
    with open(f'{file_path}', 'w') as file:
        file.write(uploaded_code_content)

#prints the output - Additional
def input_code_result(output):
    # print("OUTPUT:", output)
    pass

#runs the code - Compiler code automation (Pending)
@app.route('/run_pydemo', methods=['GET'])
def run_pydemo():
    with open('code_lang.txt', 'r') as file:
        language = file.read()
    print("Language:", language)
    compiler=compiler_list[language]
    print("Compiler bro:",compiler)
    try:
        # print("Upladed content brooo",uploaded_code_content)
        print("running code, please wait")
        result = subprocess.run(['python', f'{compiler}'], capture_output=True, text=True)
        print("run over")
        # output = result.stdout
        # print(output)
        # input_code_result(output)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#stores the langugage in which the code is needed to be converted
@app.route('/store_language', methods=['POST'])
def store_language():
    data = request.get_json()
    selected_language = data.get('language')
    content = data.get("content");
    with open("code_convertlang.txt", 'w') as file:
        file.write(selected_language)
    print("Stored bro nikallllll")
    if selected_language:
        print(f"Selected language stored: {selected_language}")
        converter(selected_language, content)
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 400



#Converts the code from one to another language
def converter(selected_language, content):
    with open('code_lang.txt', 'r') as file:
        language = file.read()
    path=language_list[language]
    # print("Path broooooooooooooooooo:",path)
    # print("Uploaded code broooooooooooo",content)
    print("COnversion staredd broooo    ")
    prompt=f"You are a code converter, your job is to convert the code from one language to another as per the specification. Convert the below given code from {language} to {selected_language}. Code: {content}.NOTE: REmove the addition description and provide only the code.IMPORTANT: Don't even generate which language it is getting converted to."
    response = model.generate_content(prompt)
    print("conversion end brooooo")
    # converted_code=response.text
    # print(converted_code.split("'''"))
    st_data(response.text)
    # converted_code=response.text
    return response.text    

#stores the converted code to its corresponding extension file (Pending full) 
def st_data(converted_code):
    language1=""
    with open("code_convertlang.txt","r") as file:
        language1=file.read()
    file_path=converter_code_file[f"{language1}"]
    # print("Converted code to be stored", language1)
    # print("File path for converted code:............",file_path)
    with open(f'{file_path}', 'w') as file1:
        file1.write(converted_code)
    print("stored broooo")
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Remove the first and last lines
    lines = lines[1:-1]
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print("First and last lines removed successfully.")

#Calls the function of converting the language from one to another language   
@app.route('/convert_code', methods=['POST'])
def convert_code():
    data = request.get_json()
    selected_language = data.get('language')
    content = data.get('content')
    print("selecteddddddddd",selected_language)
    if selected_language:
        converted_code = converter(selected_language, content)
        return jsonify({"converted_code": converted_code}), 200
    else:
        return jsonify({"error": "Language not specified"}), 400

      
#Generates the functionality page content    
@app.route('/functionality')
def functionality():
    prompt=f"You are a code analyzer, you job is to review the below given code and provide the brief response about main purpose of why this code can be used: {code_data}"
    "Note: Remove the additional description about the project and provide only the required details"
    response = model.generate_content(prompt)
    return render_template('index11.html', code_data = response.text)

#Generates the loophole page content
@app.route('/loopholes')
def loopholes():
    prompt=f"You are a Cyber security engineer, your job is to review the below given code and provide the brief response about Loop holes that are available in the code and also the Errors from the code: {code_data}"
    "Note: Remove the additional description from the response and provide only the required details"
    "IMPORTANT: Don't provide any revised code!!"
    response = model.generate_content(prompt)
    return render_template('index12.html', code_data=response.text)

#generates the optimization page content
@app.route('/optimization')
def optimization():
    prompt=f"You are a Software Developer, your job is to review the below given code and provide the brief response about optimistic ways in which the code can be modified to increase the performance: {code_data}"
    "Note: Remove the additional description from the response and provide only the required details"
    response = model.generate_content(prompt)
    return render_template('index13.html',code_data=response.text)

#Uploaded code from the Code Analyzer
@app.route('/submit_code', methods=['POST'])
def submit_code():
    global code_data
    code_data = request.json.get('code', '')
    print(code_data)
    return jsonify({"message": "Code received successfully"}), 200
# if __name__ == '__main__':
#     app.run(debug=True)
