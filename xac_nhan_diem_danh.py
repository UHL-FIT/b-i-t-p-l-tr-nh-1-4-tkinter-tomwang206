import tkinter as tk
from datetime import datetime
from tkinter import messagebox
def xu_ly_du_lieu():
    # Lấy dữ liệu từ các ô nhập
    data_maSV = o_nhap_maSV.get()
    data_hoten = o_nhap_hoten.get()

    # Lấy thời gian 
    time = datetime.now().strftime("%H:%M:%S")

    # In ra terminal để check
    print(f"{time}\nDữ liệu nhận được: \nMã sinh viên: {data_maSV}\nHọ tên: {data_hoten}\n")
    
    # 3. Cập nhật trực tiếp lên giao diện (Label kết quả)
    if data_maSV != "": 
        if data_maSV.isdigit():
            if data_hoten != "":
                messagebox.showinfo("Thông báo", f"Hello {data_hoten} - Mã sinh viên: {data_maSV}")
                 # Xóa trắng ô nhập sau khi ấn nút và in kêt quả
                o_nhap_maSV.delete(0, tk.END)
                o_nhap_hoten.delete(0, tk.END)
                o_nhap_maSV.focus()
            else: 
                messagebox.showerror("Lỗi", "Vui lòng không để trống họ tên!")
                o_nhap_hoten.focus()
        else: 
            messagebox.showerror("Lỗi", "Mã sinh viên phải là số!")
            o_nhap_maSV.delete(0, tk.END)
            o_nhap_maSV.focus()
    else: 
        messagebox.showerror("Lỗi", "Vui lòng không để trống mã sinh viên!")
        o_nhap_maSV.focus()

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1,weight=1)

# --- Tạo các thành phần, căn lề, khoảng cách, auto resize ---
# Phần mã sinh viên
nhan_maSV = tk.Label(root, text="Mã sinh viên:")
nhan_maSV.grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_maSV = tk.Entry(root)
o_nhap_maSV.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Phần họ tên
nhan_hoten = tk.Label(root, text="Họ và tên:")
nhan_hoten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_hoten = tk.Entry(root)
o_nhap_hoten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- Nút bấm ---
# Nút bấm kết nối với hàm xử lý dữ liệu
nut_xac_nhan = tk.Button(root, text="Điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()



