# Animal Skin Disease Prediciton Application
Animal Skin Disease Prediciton Application เป็นแอปพลิเคชันที่จะช่วยวิเคราะห์โรคผิวหนังของสัตว์ โดยจำแนกอาการจากภาพถ่ายของสัตว์ที่มีอาการผิดปกติ เช่น รอยแผล, การเปลี่ยนแปลงของผิวหนัง หรืออาการอื่นๆ เพื่อประเมินประเภทของโรคผิวหนังที่สัตว์อาจเป็น และสามารถแสดงผลการวิเคราะห์ พร้อมคำแนะนำในการดูแลเบื้องต้น 

# Machine Learning Techniques
- Deep Learning เป็นเทคนิคที่ทำให้โมเดลสามารถเรียนรู้จากข้อมูลจำนวนมากได้ โดยเรียนรู้จากภาพที่ได้รับ
- Image Classification: จำแนกประเภทโรคผิวหนังของสัตว์จากรูปภาพ โดยจะวิเคราะห์ลักษณะของภาพ เช่น รอยแผล หรือการเปลี่ยนแปลงของผิวหนัง เพื่อตัดสินว่าเป็นโรคอะไร
- Convolutional Neural Network (CNN): ประมวลผลภาพและเรียนรู้ลักษณะเฉพาะของภาพ เช่น รูปแบบและลวดลายที่เกี่ยวข้องกับโรคผิวหนังของสัตว์ ช่วยให้สามารถจำแนกโรคผิวหนังได้แม่นยำมากขึ้น
- Transfer Learning เป็นโมเดลที่มีการเรียนรู้ล่วงหน้ามาแล้วบนชุดข้อมูลที่มีขนาดใหญ่และหลากหลาย แล้วนำมาปรับใช้กับการจำแนกโรคผิวหนังของสัตว์ ซึ่งช่วยให้โมเดลสามารถจำแนกประเภทของโรคได้ดียิ่งขึ้น
- Supervised Learning เป็นโมเดลที่ได้รับการเรียนรู้จากข้อมูลที่มีการระบุประเภทโรคผิวหนังของสัตว์ที่เกี่ยวข้องแล้ว เพื่อประเมินว่าโรคผิวหนังในรูปภาพคือโรคอะไร ซึ่งเรียนรู้จากข้อมูลที่มีการระบุไว้ล่วงหน้า
- Evaliation Metrics ประเมินประสิทธิภาพของโมเดลในการจำแนกโรคผิวหนังของสัตว์ใช้เกณฑ์การวัดผลต่างๆ ได้แก่ Accuracy, Precision, Recall, F1-Score และ Confusion Matrix ซึ่งช่วยในการประเมินว่าโมเดลทำงานได้ดีแค่ไหนและสามารถปรับปรุงได้ในจุดไหนบ้าง

# Programming Language  
- ใช้ Python เป็นภาษาหลักที่ใช้ในการพัฒนาโมเดล CNN และการประมวลผลข้อมูล

# App Development Framework
- Kivy พัฒนา Graphical User Interface (GUI) สำหรับแอปพลิเคชัน โดยสามารถรองรับการอัปโหลดภาพโรคผิวหนังของสัตว์ และแสดงผลการวิเคราะห์จากโมเดล CNN

# Libraries 
- Tensorflow / Keras ออกแบบ สร้าง และฝึกฝนโมเดล CNN สำหรับการจำแนกโรคผิวหนังของสัตว์จากภาพที่นำเข้า
- OpenCV ประมวลผลภาพ เช่น การปรับขนาดภาพ การตัดขอบ และทำ Normalization เพื่อเตรียมข้อมูลภาพสำหรับโมเดล
- Numpy จัดการข้อมูลภาพและการเตรียมข้อมูลที่จำเป็นให้พร้อมสำหรับการฝึกโมเดล โดยสามารถคำนวณ, จัดการอาเรย์ และปรับข้อมูลให้เหมาะสมกับโมเดล CNN
- Pandas จัดการข้อมูลที่เกี่ยวข้องกับการฝึกโมเดลและผลลัพธ์ที่ได้จากโมเดล โดยเฉพาะจัดการข้อมูลในรูปแบบตาราง (DataFrame) ที่ใช่ในการฝึกโมเดลและผลลัพธ์ที่ได้จากโมเดล เช่น การโหลดข้อมูล, การวิเคราะห์ข้อมูล, การจัดเก็บข้อมูล
- Matplotlib สร้างกราฟและแผนภูมิที่ใช้ในการวิเคราะห์ผลลัพธ์ของโมเดล โดยสามารถแสดงผลของประสิทธิภาพของโมเดล เช่น การแสดงค่าความแม่นยำ (Accuracy), ความสูญเสีย (loss) หรือการเปรียบเทียบประสิทธิภาพระหว่างโมเดลต่างๆ

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
