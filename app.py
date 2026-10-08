import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản Lý Điểm Sinh Viên", layout="wide")

# 1. Hiển thị tiêu đề
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

# Tính tổng kết và xếp loại
df['Tổng kết'] = (0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']).round(2)

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
st.subheader("📋 Bảng điểm của 10 sinh viên")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# 3. Hiển thị điểm TB, sinh viên cao nhất, thấp nhất, số SV đạt
st.subheader("📊 Thống kê của lớp")
dtb_lop = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum()

st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên có điểm tổng kết cao nhất:** {sv_max['Họ tên']} ({sv_max['Tổng kết']} điểm)")
st.write(f"- **Sinh viên có điểm tổng kết thấp nhất:** {sv_min['Họ tên']} ({sv_min['Tổng kết']} điểm)")
st.write(f"- **Số sinh viên đạt (điểm tổng kết ≥ 5):** {so_sv_dat} sinh viên")

st.markdown("---")

# 4. Danh sách xổ xuống (Selectbox) và chi tiết sinh viên
st.subheader("🔍 Tra cứu chi tiết sinh viên")
selected_sv = st.selectbox("Chọn sinh viên:", df['Họ tên'])

if selected_sv:
    tt = df[df['Họ tên'] == selected_sv].iloc[0]
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Chuyên cần", tt['Chuyên cần'])
    c2.metric("Giữa kỳ", tt['Giữa kỳ'])
    c3.metric("Cuối kỳ", tt['Cuối kỳ'])
    c4.metric("Điểm tổng kết", tt['Tổng kết'])
    c5.metric("Xếp loại", tt['Xếp loại'])

st.markdown("---")

# 5. Biểu đồ cột điểm tổng kết của 10 sinh viên
st.subheader("📈 Biểu đồ cột điểm tổng kết")
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

# 6. Họ tên và MSSV ở cuối trang (chữ nhỏ)
st.caption("<small>Ứng dụng được tạo bởi: <b>Trần Lê Trọng Khánh</b> - MSSV: <b>051207000564</b></small>", unsafe_allow_html=True)
