import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản Lý Điểm Sinh Viên", layout="wide")

# 1. Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")

# Dữ liệu 10 sinh viên
data = {
    'Họ tên': [
        'Nguyễn Văn An', 'Trần Thị Bình', 'Lê Văn Chi', 'Phạm Thị Dũng', 'Hoàng Văn Hà',
        'Vũ Thị Lan', 'Đặng Văn Minh', 'Bùi Thị Nam', 'Đỗ Văn Phúc', 'Ngô Thị Trang'
    ],
    'Chuyên cần': [9.0, 8.5, 7.0, 6.5, 10.0, 8.0, 5.5, 9.5, 7.5, 8.0],
    'Giữa kỳ':    [8.0, 7.5, 6.0, 5.0,  9.0, 7.0, 6.0, 8.5, 8.0, 7.0],
    'Cuối kỳ':    [8.5, 9.0, 6.5, 4.5,  9.5, 8.0, 5.0, 9.0, 7.0, 7.5]
}

df = pd.DataFrame(data)

# Điểm tổng kết = 20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ
df['Tổng kết'] = (0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']).round(2)

# Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 2. Hiển thị bảng điểm của 10 sinh viên
st.subheader("📋 Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# 3. Thống kê
st.subheader("📊 Thống kê chung của lớp")
col1, col2, col3, col4 = st.columns(4)

dtb_lop = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum()

col1.metric("Điểm TB của lớp", f"{dtb_lop:.2f}")
col2.metric("Điểm cao nhất", f"{sv_max['Tổng kết']}", f"{sv_max['Họ tên']}")
col3.metric("Điểm thấp nhất", f"{sv_min['Tổng kết']}", f"{sv_min['Họ tên']}")
col4.metric("Số sinh viên đạt", f"{so_sv_dat}/{len(df)}")

st.markdown("---")

# 4. Danh sách xổ xuống chọn sinh viên
st.subheader("🔍 Tra cứu sinh viên")
selected_sv = st.selectbox("Chọn một sinh viên:", df['Họ tên'])

if selected_sv:
    tt = df[df['Họ tên'] == selected_sv].iloc[0]
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Chuyên cần", tt['Chuyên cần'])
    c2.metric("Giữa kỳ", tt['Giữa kỳ'])
    c3.metric("Cuối kỳ", tt['Cuối kỳ'])
    c4.metric("Điểm tổng kết", tt['Tổng kết'])
    c5.metric("Xếp loại", tt['Xếp loại'])

st.markdown("---")

# 5. Biểu đồ cột
st.subheader("📈 Biểu đồ cột điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Họ tên'], df['Tổng kết'], color='#5b9bd5', height=0.6)
ax.invert_yaxis()
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ tên sinh viên")
ax.set_xlim(0, 10)
for idx, val in enumerate(df['Tổng kết']):
    ax.text(val + 0.1, idx, str(val), va='center', fontsize=9)
st.pyplot(fig)

st.markdown("---")

# 6. Họ tên và MSSV người tạo (Sửa lại họ tên và MSSV của bạn tại đây)
st.caption("<small>Ứng dụng được tạo bởi: <b>Trần Lê Trọng Khánh</b> - MSSV: <b>051207000564</b></small>", unsafe_allow_html=True)
