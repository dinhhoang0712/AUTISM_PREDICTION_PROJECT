# 🧠 AUTISM_PREDICTION_PROJECT

## 📁 Cấu trúc thư mục

```bash
AUTISM_PREDICTION_PROJECT/
│
├── data/
│   ├── raw/                     # Dữ liệu gốc chưa xử lý
│   │   └── train.csv
│   └── processed/               # Dữ liệu sau khi làm sạch, mã hóa
│       └── data_processed.csv
│
├── documentation/               # Tài liệu mô tả, thông tin dự án
│   ├── info.txt
│
│
├── notebooks/                   # Notebook Jupyter để thực nghiệm
│   ├── 1_preprocessing.ipynb            # Bước 1: tiền xử lý
│   ├── 2_dimensionality_reduction.ipynb # Bước 2: giảm chiều dữ liệu
│   ├── 3_clustering.ipynb               # Bước 3: phân cụm (unsupervised)
│   ├── 4_classification.ipynb           # Bước 4: phân loại (supervised)
│   └── 5_regression_conversion.ipynb    # Bước 5: hồi quy hoặc chuyển đổi dữ liệu
│   src/                         # Mã nguồn Python tái sử dụng
│   ├── __init__.py
│   └── preprocessing.py
│
├── presentation/                # Thuyết trình kết quả
│   └── Presentation.pptx
│
├── report/                      # Báo cáo chính thức
│   └── Bao_cao_Autism_Prediction.docx
```

---

## 🧩 Giải thích cấu trúc

### 📂 `data/`

Chứa toàn bộ dữ liệu sử dụng trong dự án:

- **raw/**: Dữ liệu gốc chưa qua xử lý (`train.csv`).
- **processed/**: Dữ liệu đã được làm sạch, mã hóa hoặc chuẩn hóa (`data_processed.csv`).  
  👉 Giúp phân biệt rõ dữ liệu gốc và dữ liệu đã xử lý, dễ dàng tái hiện hoặc tiếp tục thực nghiệm.

---

### 📓 `notebooks/`

Chứa các notebook Jupyter tương ứng với từng giai đoạn thực nghiệm:

1. **1_preprocessing.ipynb** – Tiền xử lý dữ liệu.
2. **2_dimensionality_reduction.ipynb** – Giảm chiều dữ liệu.
3. **3_clustering.ipynb** – Phân cụm (unsupervised learning).
4. **4_classification.ipynb** – Phân loại (supervised learning).
5. **5_regression_conversion.ipynb** – Hồi quy hoặc chuyển đổi dữ liệu.

👉 Mỗi notebook đại diện cho một bước trong quy trình nghiên cứu, giúp dễ theo dõi, kiểm tra và tái hiện kết quả.

---

### 🧠 `src/`

Chứa các mã nguồn Python được tái sử dụng nhiều lần:

- Các hàm xử lý dữ liệu, chuẩn hóa, mã hóa biến.
- Các mô-đun huấn luyện mô hình và hỗ trợ trực quan hóa.

👉 Giúp mã nguồn gọn gàng, dễ bảo trì và có thể import vào notebook mà không cần viết lại.

---

### 📜 `documentation/`

Lưu trữ tài liệu mô tả và hướng dẫn kỹ thuật:

- **info.txt** – Thông tin về dữ liệu, định dạng, nguồn gốc.
- **README.txt** – Hướng dẫn chạy, mô tả cấu trúc và mục đích của dự án.

👉 Giúp người dùng hoặc giảng viên hiểu nhanh cách triển khai và tái hiện dự án.

---

### 🖼️ `presentation/` & 🧾 `report/`

- **presentation/**: Chứa file trình chiếu kết quả thực nghiệm (`Presentation.pptx`).
- **report/**: Chứa báo cáo chính thức (`Bao_cao_Autism_Prediction.docx`).

👉 Giúp tách biệt phần kỹ thuật (data, code, notebook) với phần trình bày và báo cáo kết quả.

---

## 🚀 Cách chạy dự án

### 1️⃣ Yêu cầu hệ thống

- Python ≥ 3.0
- Jupyter Notebook hoặc JupyterLab
- Thư viện Python: pandas, numpy, scikit-learn, imbalanced-learn, matplotlib, seaborn, plotly, umap-learn, scipy

---

### 2️⃣ Cách thực hiện

1. Clone hoặc tải dự án về máy:
   ```bash
   git clone https://github.com/dinhhoang0712/AUTISM_PREDICTION_PROJECT.git
   ```
2. Mở thư mục dự án trong VSCode hoặc Jupyter.
3. Mở và chạy lần lượt các notebook trong thư mục `notebooks/` theo thứ tự:
   - `1_preprocessing.ipynb` → `2_dimensionality_reduction.ipynb` → `3_clustering.ipynb` → `4_classification.ipynb` → `5_regression_conversion.ipynb`.
4. Kết quả trung gian và mô hình sẽ được lưu trong các thư mục tương ứng (hoặc hiển thị trực tiếp trong notebook).
