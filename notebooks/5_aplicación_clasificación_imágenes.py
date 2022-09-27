import streamlit as st
import torch
import torch.nn.functional as F

from PIL import Image

import torchvision
from torchvision import transforms

import time


preprocess= transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.3452, 0.3810, 0.4083),
                             (0.2036, 0.1367, 0.1150)),
        transforms.Resize(size=(64, 64))
    ])


efficientnet = torchvision.models.efficientnet_b0(weights="IMAGENET1K_V1")
efficientnet.classifier[1] = torch.nn.Linear(in_features = 1280, out_features = 10)

efficientnet.load_state_dict(torch.load('efficientnet.pt', map_location=torch.device('cpu')))
                                        
                           

class_names = ["Annual Crop", "Forest", "Herbaceous Vegetation", "Highway", "Industrial", "Pasture", "Permanent Crop",
"Residential", "River", "Mar Lago"]
       
# Designing the interface
st.title("Clasificación imágenes de satélite App")
# For newline
st.write('\n')

#Disabling warning
st.set_option('deprecation.showfileUploaderEncoding', False)
#Choose your own image
uploaded_file = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg'] )

if uploaded_file is not None:
    u_img = Image.open(uploaded_file)
    
    show = st.image(u_img, use_column_width=True)
    # show.image(u_img, 'Imagen subida!', use_column_width=True)
    # We preprocess the image to fit in algorithm.
    image = preprocess(u_img).unsqueeze(0)
    print(image.size)
    
    
# For newline
st.sidebar.write('\n')
    
if st.sidebar.button("Presiona para clasificar"):
    
    if uploaded_file is None:
        
        st.sidebar.write("Por favor, sube una imagen para clasificar")
    
    else:
        
        with st.spinner('Clasificando ...'):
            
            with torch.no_grad():
            	efficientnet.eval()
            	out = efficientnet(image)
            _, prediction = torch.max(out, dim=1)
            print(prediction)
            print(out)
            print(F.softmax(out, dim=1))
            out = out.squeeze(0)
            probability = F.softmax(out, dim=0)[prediction]
            time.sleep(2)
            st.success('Hecho!')
            
        st.sidebar.header("La red predice: ")
        
        #Formatted probability value to 3 decimal places
        probability = "{:.3f}".format(float(probability*100))
        
        # Classify cat being present in the picture if prediction > 0.5
        
        st.sidebar.write("It's ", class_names[prediction], ".\n" )
        st.sidebar.write('**Probability: **',probability,'%')
                             
    
    
