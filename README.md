# Animal Skin Disease Prediction Application
Animal Skin Disease Prediciton Application เป็นแอปพลิเคชันที่จะช่วยวิเคราะห์โรคผิวหนังของสัตว์ โดยจำแนกอาการจากภาพถ่ายของสัตว์ที่มีอาการผิดปกติ เช่น รอยแผล, การเปลี่ยนแปลงของผิวหนัง หรืออาการอื่นๆ เพื่อประเมินประเภทของโรคผิวหนังที่สัตว์อาจเป็น และสามารถแสดงผลการวิเคราะห์ พร้อมคำแนะนำในการดูแลเบื้องต้น 

# Features
- Disease Prediction: ใช้โมเดล CNN ในการวิเคราะห์ภาพโรคผิวหนังของสัตว์และจำแนกประเภทของโรค
- User-friendly Interface: มีระบบอัปโหลดภาพที่ใช้งานง่าย รองรับไฟล์ .png, .jpg, .jpeg
- Prediction Confidence: แสดงผลลัพธ์การวิเคราะห์พร้อมค่าความมั่นใจของโมเดล
- Treatment Suggestions: ให้คำแนะนำเบื้องต้นเกี่ยวกับการดูแลสัตว์เลี้ยงตามประเภทของโรค
- Result Visualization: แสดงค่าความน่าจะเป็นของแต่ละประเภทโรคในรูปแบบกราฟแท่ง

# Model Information
- Input Image Size: 224x224 pixels
- Pre-trained Model: Fine-tuned CNN
- Classes:
  - Bacterial
  - Fungal
  - Healthy
  - Hypersensitivity
- Dataset Augmentation: ใช้เทคนิคเพิ่มข้อมูลภาพเพื่อให้โมเดลมีประสิทธิภาพมากขึ้น
  
# Machine Learning Techniques
- Deep Learning สร้างและฝึกโมเดลที่ใช้ Convolutional Neural Networks (CNN) เพื่อตรวจสอบโรคผิวหนังของสัตว์จากภาพถ่ายของสัตว์ โดยโมเดลนี้สามารถเรียนรู้จากข้อมูลจำนวนมากที่มีภาพถ่ายเพื่อจำแนกโรคต่างๆ ของสัตว์ได้
- Image Classification จำแนกประเภทโรคผิวหนังของสัตว์จากรูปภาพ โดยจะวิเคราะห์ลักษณะของภาพ เช่น รอยแผล หรือการเปลี่ยนแปลงของผิวหนัง เพื่อตัดสินว่าเป็นโรคอะไร
- Convolutional Neural Network (CNN) ใช้ InceptionV3 ที่เป็น CNN Architecture ที่ฝึกมาแล้ว (pre-trained model) ด้วยข้อมูล ImageNet ซึ่งช่วยในการเรียนรู้ลักษณะเฉพาะของภาพ เช่น รูปแบบและลวดลายของโรคผิวหนังของสัตว์
- Transfer Learning ใช้ผ่านการใช้โมเดล InceptionV3 ที่ฝึกมาแล้วจาก ImageNet ซึ่งช่วยให้โมเดลสามารถเรียนรู้จากข้อมูลจำนวนมากที่มีอยู่แล้วและนำมาปรับใช้กับการจำแนกโรคผิวหนังของสัตว์ 
- Supervised Learning โมเดลได้รับข้อมูลที่มีการระบุประเภทของโรคผิวหนังที่สัมพันธ์กับภาพถ่ายที่มี ซึ่งโมเดลจะเรียนรู้จากข้อมูลที่มีการระบุประเภทไว้แล้ว
- Evaliation Metrics ใช้ Confusion Matrix เพื่อตรวจสอบว่าโมเดลสามารถจำแนกประเภทโรคได้ดีเพียงใด โดยการแสดงผลการทำนายและผลจริงในรูปแบบของ Confusion Matrix และใช้ Accuracy เป็นหนึ่งในเกณฑ์ในการวัดประสิทธิภาพของโมเดลในการจำแนกภาพ

# Programming Language  
- Python ใช้เป็นภาษาหลักที่ใช้ในการพัฒนาโมเดล CNN และการประมวลผลข้อมูล

# App Development Framework
- Kivy พัฒนา Graphical User Interface (GUI) สำหรับแอปพลิเคชัน โดยสามารถรองรับการอัปโหลดภาพโรคผิวหนังของสัตว์ และแสดงผลการวิเคราะห์จากโมเดล CNN

# Libraries 
- Tensorflow / Keras ออกแบบ สร้าง และฝึกฝนโมเดล CNN สำหรับการจำแนกโรคผิวหนังของสัตว์จากภาพที่นำเข้า
- OpenCV ประมวลผลภาพ เช่น การปรับขนาดภาพ การตัดขอบ และทำ Normalization เพื่อเตรียมข้อมูลภาพสำหรับโมเดล
- Numpy จัดการข้อมูลภาพและการเตรียมข้อมูลที่จำเป็นให้พร้อมสำหรับการฝึกโมเดล โดยสามารถคำนวณ, จัดการอาเรย์ และปรับข้อมูลให้เหมาะสมกับโมเดล CNN
- Pandas จัดการข้อมูลที่เกี่ยวข้องกับการฝึกโมเดลและผลลัพธ์ที่ได้จากโมเดล โดยเฉพาะจัดการข้อมูลในรูปแบบตาราง (DataFrame) ที่ใช้ในการฝึกโมเดลและผลลัพธ์ที่ได้จากโมเดล เช่น การโหลดข้อมูล, การวิเคราะห์ข้อมูล, การจัดเก็บข้อมูล
- Matplotlib สร้างกราฟและแผนภูมิที่ใช้ในการวิเคราะห์ผลลัพธ์ของโมเดล โดยสามารถแสดงผลของประสิทธิภาพของโมเดล เช่น การแสดงค่าความแม่นยำ (Accuracy), ความสูญเสีย (loss) หรือการเปรียบเทียบประสิทธิภาพระหว่างโมเดลต่างๆ
- Shutil คัดลอกและย้ายไฟล์ที่ผู้ใช้อัปโหลด เพื่อจัดเก็บภาพที่ได้รับการวิเคราะห์แล้วในโฟลเดอร์ที่กำหนด
- Datetime สร้างชื่อไฟล์ที่ไม่ซ้ำกัน โดยแนบวันและเวลาปัจจุบันกับชื่อไฟล์เพื่อให้แต่ละไฟล์ที่อัปโหลดมีชื่อที่แตกต่างกัน
- Kivy Clock หน่วงเวลาการประมวลผลภาพ เพื่อให้ UI ตอบสนองได้ดีขึ้นและไม่ทำให้แอปพลิเคชันค้างขณะทำงาน
- OS จัดการเส้นทางไฟล์และโฟลเดอร์สำหรับเก็บภาพที่อัปโหลด เช่น ตรวจสอบว่าโฟลเดอร์หรือไฟล์มีอยู่หรือไม่ และสร้างโฟลเดอร์หากยังไม่มี เป็นต้น

# Directory Structure

```sh
Image_Processor/
│
├── Test/                   # โฟลเดอร์สำหรับเก็บข้อมูลทดสอบ
│   ├── Bacterial/          # ข้อมูลทดสอบโรคแบคทีเรีย
│   ├── Fungal/             # ข้อมูลทดสอบโรคเชื้อรา
│   ├── Healthy/            # ข้อมูลทดสอบสัตว์ที่สุขภาพดี
│   └── Hypersensitivity/   # ข้อมูลทดสอบโรคภูมิไวเกิน
│
├── Train/                  # โฟลเดอร์สำหรับเก็บข้อมูลฝึกสอน
│   ├── Bacterial/          # ข้อมูลฝึกสอนโรคแบคทีเรีย
│   ├── Fungal/             # ข้อมูลฝึกสอนโรคเชื้อรา
│   ├── Healthy/            # ข้อมูลฝึกสอนสัตว์ที่สุขภาพดี
│   └── Hypersensitivity/   # ข้อมูลฝึกสอนโรคภูมิไวเกิน
│
├── Validation/             # โฟลเดอร์สำหรับเก็บข้อมูลการตรวจสอบโมเดล
│   ├── Bacterial/          # ข้อมูลการตรวจสอบโรคแบคทีเรีย
│   ├── Fungal/             # ข้อมูลการตรวจสอบโรคเชื้อรา
│   ├── Healthy/            # ข้อมูลการตรวจสอบสัตว์ที่สุขภาพดี
│   └── Hypersensitivity/   # ข้อมูลการตรวจสอบโรคภูมิไวเกิน
│
├── AnimalSkinDiseasePrediction_Model.ipynb  # Jupyter notebook สำหรับการฝึกและสร้างโมเดล
├── LICENSE.md                               # ไฟล์กำหนดเงื่อนไขการใช้งานโปรเจกต์
├── README.md                                # ไฟล์ที่ให้ข้อมูลเกี่ยวกับโปรเจกต์
├── asdp.kv                                  # ไฟล์ Kivy สำหรับออกแบบ UI ของแอปพลิเคชัน
├── asdpapp.py                               # ไฟล์หลักของแอปพลิเคชันที่ใช้จัดการ UI และโมเดล
└── model1/                                  # โฟลเดอร์ที่เก็บโมเดลที่ดีที่สุดที่ได้รับการฝึกมาแล้ว
```

# Setup

```sh
pip install kivy tensorflow numpy
```

# Usage
- AnimalSkinDiseasePrediciton_Model.ipynb
- โมเดลที่ใช้ InceptionV3 โดยมีการล็อคเลเยอร์จาก InceptionV3 ทั้งหมด (ไม่ให้ฝึก) และแค่ฝึกเลเยอร์ที่เพิ่มเข้ามาใหม่ เช่น Dense และ Dropout
- หลังจากฝึกฝนเสร็จแล้ว จะมีการบันทึกโมเดลที่ดีที่สุด (ModelCheckpoint) และหยุดฝึกถ้าโมเดลไม่ดีขึ้นหลังจากหลายๆ epoch (EarlyStopping)

```sh
filepath = "/content/drive/MyDrive/AnimalSkinDiseasePrediciton/model2/model_fit_{epoch:02d}-{val_accuracy:.2f}.keras"
checkpoint1 = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
early = EarlyStopping(monitor="acc", mode="max", patience=15)

callbacks_list = [checkpoint1, early] #early
```

- โมเดลนี้มีการ fine-tune โดยการปลดล็อคเลเยอร์บางส่วนของ InceptionV3 เพื่อให้โมเดลสามารถปรับปรุงในส่วนของ InceptionV3 ด้วย
- ในขั้นตอนนี้จะมีการฝึกโมเดลใหม่อีกครั้งโดยใช้ callbacks เหมือนเดิม ได้แก่ ModelCheckpoint และ EarlyStopping
  
```sh
filepath = "/content/drive/MyDrive/AnimalSkinDiseasePrediciton/model1/model_finetuned1_{epoch:02d}-{val_accuracy:.2f}.keras"
checkpoint1 = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
early = EarlyStopping(monitor="acc", mode="max", patience=15)

callbacks_list = [checkpoint1, early] #early
```

- โหลดโมเดลที่ดีที่สุดที่ฝึกจาก epoch ที่ดีที่สุด
- โดยสังเกตจากชื่อไฟล์โมเดล (model_fit_19-0.96.keras) แสดงว่าโมเดลนี้ได้ผลลัพธ์ที่ดีที่สุดใน epoch 19 ด้วย validation accuracy 96%

```sh
best_model_finetuned = load_model('/content/drive/MyDrive/AnimalSkinDiseasePrediciton/model1/model_finetuned1_19-0.96.keras')
```

- asdpapp.py
- โหลดโมเดลที่ดีที่สุด (best model) มาใช้งานบนแอปพลิเคชัน เพื่อทำนายว่าอาการนั้นเป็นโรคอะไร

```sh
def load_model(self):
    try:
        model_path = 'C:\\Users\\asus\\OneDrive\\Desktop\\เอกสาร\\241-202\\asdpapp\\model1\\model_finetuned1_19-0.96.keras'
        self.model = load_model(model_path)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
        self.show_error_popup(f"Failed to load model: {e}")
```

# Getting Started
- Clone the repository

```sh
git clone https://github.com/JULHMSPLOY/Animal_Skin_Disease_Prediciton_Application.git
```

- Install dependencies
```sh
pip install -r requirements.txt
```

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
