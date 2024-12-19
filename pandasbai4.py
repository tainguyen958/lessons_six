class StudentManager(object):
    def __init__(self):
        self.danh_sach_hoc_sinh = {}

    def them_hoc_sinh(self, name, score):
        if name in self.danh_sach_hoc_sinh:
            print(f"Học sinh {name} đã tồn tại.")
        else:
            self.danh_sach_hoc_sinh[name] = score

    def xoa_hoc_sinh(self, name):
        if name in self.danh_sach_hoc_sinh:
            del self.danh_sach_hoc_sinh[name]
        else:
            print(f"Không tìm thấy học sinh {name}.")

    def cap_nhat_diem(self, name, new_score):
        if name in self.danh_sach_hoc_sinh:
            self.danh_sach_hoc_sinh[name] = new_score
        else:
            print(f"Không tìm thấy học sinh {name}.")

    def tinh_diem_trung_binh_tung_hoc_sinh(self):
        ket_qua = {}
        for name, score in self.danh_sach_hoc_sinh.items():
            if score:
                score_tb = sum(score) / len(score)
                ket_qua[name] = score_tb
        return ket_qua

    def tinh_diem_trung_binh_lop(self):
        score_tb = self.tinh_diem_trung_binh_tung_hoc_sinh()
        if score_tb:
            return sum(score_tb.values()) / len(score_tb)
        return 0

    def hien_thi_danh_sach(self):
        for name, score in self.danh_sach_hoc_sinh.items():
            score_tb = sum(score) / len(score) if score else 0
            print(f"{name}: {score} (Điểm TB: {score_tb:.2f})")

    def loc_hoc_sinh_theo_diem_tb(self, nguong):
        return {name: score for name, score in self.tinh_diem_trung_binh_tung_hoc_sinh().items() if score >= nguong}

quan_ly = StudentManager()
quan_ly.them_hoc_sinh("Nguyen Van A", [8, 9, 7])
quan_ly.them_hoc_sinh("Le Thi B", [6, 5, 7])
quan_ly.them_hoc_sinh("Tran Van C", [10, 9])

quan_ly.hien_thi_danh_sach()
print("\nCập nhật điểm:")
quan_ly.cap_nhat_diem("Le Thi B", [7, 8, 6])

quan_ly.hien_thi_danh_sach()
print("\nĐiểm trung bình lớp:", quan_ly.tinh_diem_trung_binh_lop())

print("\nHọc sinh có điểm trung bình >= 7:")
loc = quan_ly.loc_hoc_sinh_theo_diem_tb(7)
for ten, diem_tb in loc.items():
    print(f"{ten}: {diem_tb:.2f}")