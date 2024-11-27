import google.generativeai as genai
genai.configure(api_key="AIzaSyATWFJFyhguScg6T0M1CeBj8hlu6Qpg4EQ")

for model_info in genai.list_tuned_models():
    print(model_info.name)
    
model = genai.GenerativeModel(model_name="tunedModels/elsujeto-edbj9h3si2ku")
result = model.generate_content("""12 El sistema deberá responder a todas las solicitudes de los usuarios en un tiempo máximo de 2 segundos.""")
print(result.text)  # IV

