from PIL import Image
from tensorflow.keras import models
import numpy as np
from fastapi import FastAPI, File
import os
from io import BytesIO

app = FastAPI()
app.state.model_cataract = models.load_model('api/models/cataract')
app.state.model_glaucoma = models.load_model('api/models/glaucoma')
app.state.model_myopia = models.load_model('api/models/myopia')


@app.post('/predict')
async def predict(file: bytes = File()):
    content = file
    im = Image.open(BytesIO(content))
    img = im.resize((224, 224))
    img_array = np.array(img)  # convert PIL Image to numpy array
    image = img_array.reshape((-1, 224, 224, 3))
    prediction_cataract = app.state.model_cataract.predict(image)
    prediction_glaucoma = app.state.model_glaucoma.predict(image)
    prediction_myopia = app.state.model_myopia.predict(image)

    result = {'cataract': round((1-prediction_cataract[0][0])*100,2),'glaucoma':
        round((1-prediction_glaucoma[0][0])*100,2),'myopia': round((1-prediction_myopia[0][0])*100,2)}
    return result
