# CareerLift: danh sách màn hình

Tài liệu này liệt kê mọi màn hình và trạng thái giao diện của app, chia theo 3 module ở thanh menu: **Kiến thức**, **Phỏng vấn thử**, **Cài đặt**. Mỗi màn hình có ảnh desktop (rộng 1280px) và mobile (rộng 390px), chụp ở giao diện tối, tiếng Việt.

- **Dữ liệu trong ảnh là dữ liệu mẫu.** Các trạng thái cần AI (chấm điểm, gợi ý, phân tích JD, phòng phỏng vấn, báo cáo) được giả lập nên không cần API key để tái tạo.
- **Đường dẫn** trong cột Route là phần sau dấu `#` của URL. Mở trực tiếp đường dẫn đó sẽ vào đúng màn hình, tải lại trang vẫn giữ nguyên chỗ.
- **Thành phần dùng chung:** thanh trên cùng có logo và nút đổi ngôn ngữ EN/VI. Trên desktop, menu nằm ở thanh trên; trên mobile (dưới 720px), menu chuyển xuống đáy màn hình.

## Mục lục

- [1. Kiến thức](#1-kiến-thức) (20 trạng thái)
- [2. Phỏng vấn thử](#2-phỏng-vấn-thử) (15 trạng thái)
- [3. Cài đặt](#3-cài-đặt) (4 trạng thái)
- [Chụp lại ảnh](#chụp-lại-ảnh)

---

## 1. Kiến thức

| # | Màn hình | Route | Nội dung chính |
|---|---|---|---|
| K01 | Trang chính Kiến thức | `#/` | Card thẻ cần ôn hôm nay, card bài học tiếp theo, danh sách 6 chủ đề kèm tiến độ, nút Thêm bài học bằng AI |
| K02 | Chủ đề: tab Bài học | `#/topic/{id}/lessons` | Danh sách bài (đã học có ✓, bài AI tạo có nhãn), nút Thêm bài học bằng AI |
| K03 | Chủ đề: tab Thẻ ghi nhớ | `#/topic/{id}/cards` | Số thẻ đến hạn, nút Ôn N thẻ và Ôn lại toàn bộ, danh sách thẻ với lịch ôn |
| K04 | Chủ đề: tab Luyện trả lời | `#/topic/{id}/practice` | Danh sách câu hỏi kèm điểm cao nhất, nút Tạo câu hỏi mới bằng AI |
| K05 | Chủ đề: tab Trắc nghiệm | `#/topic/{id}/quiz` | Giới thiệu bài test, lịch sử điểm, nút làm bài và tạo đề bằng AI |
| K06 | Đọc bài học | `#/lesson/{id}` | Nội dung bài, ô hỏi AI, nút đánh dấu đã học và bài tiếp theo |
| K07 | Đọc bài học: đã hỏi AI | `#/lesson/{id}` | Câu trả lời của AI cho câu hỏi về bài |
| K08 | Thêm bài học bằng AI | `#/new-lesson` | Ô nhập đề tài, gợi ý đề tài, chọn chủ đề, nút Tạo bài học |
| K09 | Thêm bài học: đang viết | `#/new-lesson` | Trạng thái chờ AI viết bài (30 đến 60 giây) |
| K10 | Ôn thẻ: mặt trước | `#/review` | Câu hỏi trên thẻ, chạm để lật |
| K11 | Ôn thẻ: mặt sau | `#/review` | Đáp án và 4 mức đánh giá (Chưa nhớ, Hơi nhớ, Nhớ rồi, Quá dễ) |
| K12 | Ôn thẻ: AI giải thích | `#/review` | Ví dụ thực tế và câu hỏi phỏng vấn liên quan do AI viết |
| K13 | Ôn thẻ: hoàn thành | `#/review` | Số thẻ đã ôn, nút luyện trả lời và về Kiến thức |
| K14 | Luyện trả lời | `#/practice/{topic}/{qid}` | Câu hỏi, đồng hồ, ô trả lời, các nút Chấm điểm bằng AI, Trả lời (ghi âm), Gợi ý |
| K15 | Luyện trả lời: mở gợi ý | `#/practice/{topic}/{qid}` | Khung "Câu trả lời tốt thường có" |
| K16 | Luyện trả lời: đang ghi âm | `#/practice/{topic}/{qid}` | Nút Dừng màu đỏ có biểu tượng hình vuông |
| K17 | Luyện trả lời: đang chấm | `#/practice/{topic}/{qid}` | Trạng thái chờ AI chấm |
| K18 | Luyện trả lời: kết quả | `#/practice/{topic}/{qid}` | Điểm, nhận xét theo tiêu chí, làm tốt, cần cải thiện, dàn ý tham khảo |
| K19 | Làm bài trắc nghiệm | `#/quiz/{topic}` | Đồng hồ đếm ngược, ô số câu, 4 đáp án. Nút chính là **Câu sau**; chỉ ở câu cuối hoặc khi đã trả lời hết mới thành **Nộp bài**. Nộp sớm bằng nút nhỏ cạnh đồng hồ |
| K20 | Trắc nghiệm: kết quả | `#/quiz/{topic}` | Điểm, nhận xét theo nhóm kiến thức, xem lại đáp án kèm khung **Giải thích** cho từng câu |

### K01. Trang chính Kiến thức
| Desktop | Mobile |
|---|---|
| <img src="screens/k01-learn-desktop.png" width="640"> | <img src="screens/k01-learn-mobile.png" width="240"> |

### K02. Chủ đề: tab Bài học
| Desktop | Mobile |
|---|---|
| <img src="screens/k02-topic-lessons-desktop.png" width="640"> | <img src="screens/k02-topic-lessons-mobile.png" width="240"> |

### K03. Chủ đề: tab Thẻ ghi nhớ
| Desktop | Mobile |
|---|---|
| <img src="screens/k03-topic-cards-desktop.png" width="640"> | <img src="screens/k03-topic-cards-mobile.png" width="240"> |

### K04. Chủ đề: tab Luyện trả lời
| Desktop | Mobile |
|---|---|
| <img src="screens/k04-topic-practice-desktop.png" width="640"> | <img src="screens/k04-topic-practice-mobile.png" width="240"> |

### K05. Chủ đề: tab Trắc nghiệm
| Desktop | Mobile |
|---|---|
| <img src="screens/k05-topic-quiz-desktop.png" width="640"> | <img src="screens/k05-topic-quiz-mobile.png" width="240"> |

### K06. Đọc bài học
| Desktop | Mobile |
|---|---|
| <img src="screens/k06-lesson-desktop.png" width="640"> | <img src="screens/k06-lesson-mobile.png" width="240"> |

### K07. Đọc bài học: đã hỏi AI
| Desktop | Mobile |
|---|---|
| <img src="screens/k07-lesson-ask-ai-desktop.png" width="640"> | <img src="screens/k07-lesson-ask-ai-mobile.png" width="240"> |

### K08. Thêm bài học bằng AI
| Desktop | Mobile |
|---|---|
| <img src="screens/k08-new-lesson-desktop.png" width="640"> | <img src="screens/k08-new-lesson-mobile.png" width="240"> |

### K09. Thêm bài học: đang viết
| Desktop | Mobile |
|---|---|
| <img src="screens/k09-new-lesson-loading-desktop.png" width="640"> | <img src="screens/k09-new-lesson-loading-mobile.png" width="240"> |

### K10. Ôn thẻ: mặt trước
| Desktop | Mobile |
|---|---|
| <img src="screens/k10-review-front-desktop.png" width="640"> | <img src="screens/k10-review-front-mobile.png" width="240"> |

### K11. Ôn thẻ: mặt sau
| Desktop | Mobile |
|---|---|
| <img src="screens/k11-review-back-desktop.png" width="640"> | <img src="screens/k11-review-back-mobile.png" width="240"> |

### K12. Ôn thẻ: AI giải thích
| Desktop | Mobile |
|---|---|
| <img src="screens/k12-review-ai-explain-desktop.png" width="640"> | <img src="screens/k12-review-ai-explain-mobile.png" width="240"> |

### K13. Ôn thẻ: hoàn thành
| Desktop | Mobile |
|---|---|
| <img src="screens/k13-review-done-desktop.png" width="640"> | <img src="screens/k13-review-done-mobile.png" width="240"> |

### K14. Luyện trả lời
| Desktop | Mobile |
|---|---|
| <img src="screens/k14-practice-desktop.png" width="640"> | <img src="screens/k14-practice-mobile.png" width="240"> |

### K15. Luyện trả lời: mở gợi ý
| Desktop | Mobile |
|---|---|
| <img src="screens/k15-practice-hint-desktop.png" width="640"> | <img src="screens/k15-practice-hint-mobile.png" width="240"> |

### K16. Luyện trả lời: đang ghi âm
| Desktop | Mobile |
|---|---|
| <img src="screens/k16-practice-recording-desktop.png" width="640"> | <img src="screens/k16-practice-recording-mobile.png" width="240"> |

### K17. Luyện trả lời: đang chấm
| Desktop | Mobile |
|---|---|
| <img src="screens/k17-practice-grading-desktop.png" width="640"> | <img src="screens/k17-practice-grading-mobile.png" width="240"> |

### K18. Luyện trả lời: kết quả
| Desktop | Mobile |
|---|---|
| <img src="screens/k18-practice-result-desktop.png" width="640"> | <img src="screens/k18-practice-result-mobile.png" width="240"> |

### K19. Làm bài trắc nghiệm
| Desktop | Mobile |
|---|---|
| <img src="screens/k19-quiz-desktop.png" width="640"> | <img src="screens/k19-quiz-mobile.png" width="240"> |

### K20. Trắc nghiệm: kết quả
| Desktop | Mobile |
|---|---|
| <img src="screens/k20-quiz-result-desktop.png" width="640"> | <img src="screens/k20-quiz-result-mobile.png" width="240"> |

---

## 2. Phỏng vấn thử

Phòng phỏng vấn dùng chung route `#/interview` với trang thiết lập: khi đang có buổi phỏng vấn dở, route này mở phòng; khi không có, nó mở trang thiết lập. Buổi đang dở được giữ lại khi tải lại trang.

| # | Màn hình | Route | Nội dung chính |
|---|---|---|---|
| I01 | Thiết lập: một vòng | `#/interview` | Danh sách JD, chọn vòng, số câu hỏi vặn, phong cách người phỏng vấn, ngôn ngữ, lịch sử phỏng vấn |
| I02 | Thiết lập: trọn quy trình | `#/interview` | Chọn nhiều vòng theo thứ tự tuyển dụng |
| I03 | Thêm JD | `#/interview` | Form tên JD, vị trí, cấp độ, loại công ty, nội dung JD |
| I04 | Phân tích JD | `#/interview` | Kỹ năng then chốt, chủ đề nên ôn, câu hỏi dễ gặp, quy trình gợi ý |
| I05 | Phòng: AI đang hỏi | `#/interview` | Câu hỏi hiện dần từng chữ, nút Dừng |
| I06 | Phòng: đến lượt trả lời | `#/interview` | Hội thoại, ô trả lời, các nút Gửi, Trả lời (ghi âm), Gợi ý, Chấm điểm ngay (bỏ qua câu hỏi vặn còn lại); nút Hủy ở đầu trang để bỏ buổi |
| I07 | Phòng: đã mở gợi ý | `#/interview` | Khung "Gợi ý hướng trả lời" dưới câu hỏi |
| I08 | Phòng: đang ghi âm | `#/interview` | Nút Dừng màu đỏ có biểu tượng hình vuông |
| I09 | Phòng: đang chấm vòng | `#/interview` | Lời kết của người phỏng vấn và trạng thái chờ chấm |
| I10 | Phòng: lỗi kết nối | `#/interview` | Thông báo lỗi và nút Hỏi lại |
| I11 | Phòng: vòng Bài test AI | `#/interview` | Bài trắc nghiệm có giờ ngay trong phòng |
| I12 | Kết quả vòng | `#/interview` | Điểm vòng, nhận xét, bản ghi, nút sang vòng sau |
| I13 | Tổng kết buổi | `#/interview` | Điểm chung, điểm từng vòng, chủ đề nên ôn, nút **Phỏng vấn mới** (chính) và Xem tổng kết nằm ngang tiêu đề |
| I14 | Báo cáo: buổi một vòng | `#/report/{id}` | Kết quả vòng đầy đủ và bản ghi |
| I15 | Báo cáo: buổi nhiều vòng | `#/report/{id}` | Phần tổng kết, sau đó là kết quả từng vòng |

### I01. Thiết lập: một vòng
| Desktop | Mobile |
|---|---|
| <img src="screens/i01-setup-desktop.png" width="640"> | <img src="screens/i01-setup-mobile.png" width="240"> |

### I02. Thiết lập: trọn quy trình
| Desktop | Mobile |
|---|---|
| <img src="screens/i02-setup-full-loop-desktop.png" width="640"> | <img src="screens/i02-setup-full-loop-mobile.png" width="240"> |

### I03. Thêm JD
| Desktop | Mobile |
|---|---|
| <img src="screens/i03-jd-form-desktop.png" width="640"> | <img src="screens/i03-jd-form-mobile.png" width="240"> |

### I04. Phân tích JD
| Desktop | Mobile |
|---|---|
| <img src="screens/i04-jd-analysis-desktop.png" width="640"> | <img src="screens/i04-jd-analysis-mobile.png" width="240"> |

### I05. Phòng: AI đang hỏi
| Desktop | Mobile |
|---|---|
| <img src="screens/i05-room-asking-desktop.png" width="640"> | <img src="screens/i05-room-asking-mobile.png" width="240"> |

### I06. Phòng: đến lượt trả lời
| Desktop | Mobile |
|---|---|
| <img src="screens/i06-room-answer-desktop.png" width="640"> | <img src="screens/i06-room-answer-mobile.png" width="240"> |

### I07. Phòng: đã mở gợi ý
| Desktop | Mobile |
|---|---|
| <img src="screens/i07-room-hint-desktop.png" width="640"> | <img src="screens/i07-room-hint-mobile.png" width="240"> |

### I08. Phòng: đang ghi âm
| Desktop | Mobile |
|---|---|
| <img src="screens/i08-room-recording-desktop.png" width="640"> | <img src="screens/i08-room-recording-mobile.png" width="240"> |

### I09. Phòng: đang chấm vòng
| Desktop | Mobile |
|---|---|
| <img src="screens/i09-room-grading-desktop.png" width="640"> | <img src="screens/i09-room-grading-mobile.png" width="240"> |

### I10. Phòng: lỗi kết nối
| Desktop | Mobile |
|---|---|
| <img src="screens/i10-room-error-desktop.png" width="640"> | <img src="screens/i10-room-error-mobile.png" width="240"> |

### I11. Phòng: vòng Bài test AI
| Desktop | Mobile |
|---|---|
| <img src="screens/i11-room-ai-test-desktop.png" width="640"> | <img src="screens/i11-room-ai-test-mobile.png" width="240"> |

### I12. Kết quả vòng
| Desktop | Mobile |
|---|---|
| <img src="screens/i12-round-result-desktop.png" width="640"> | <img src="screens/i12-round-result-mobile.png" width="240"> |

### I13. Tổng kết buổi
| Desktop | Mobile |
|---|---|
| <img src="screens/i13-final-summary-desktop.png" width="640"> | <img src="screens/i13-final-summary-mobile.png" width="240"> |

### I14. Báo cáo: buổi một vòng
| Desktop | Mobile |
|---|---|
| <img src="screens/i14-report-single-round-desktop.png" width="640"> | <img src="screens/i14-report-single-round-mobile.png" width="240"> |

### I15. Báo cáo: buổi nhiều vòng
| Desktop | Mobile |
|---|---|
| <img src="screens/i15-report-multi-round-desktop.png" width="640"> | <img src="screens/i15-report-multi-round-mobile.png" width="240"> |

---

## 3. Cài đặt

| # | Màn hình | Route | Nội dung chính |
|---|---|---|---|
| S01 | Cài đặt: chưa có key | `#/settings` | Mục tiêu học tập, form nhập Gemini API key, kết nối Google Drive, nút xóa tiến độ |
| S02 | Cài đặt: đã lưu key | `#/settings` | Model đang dùng và nút Xóa API key |
| S03 | Cài đặt: sửa mục tiêu học tập | `#/settings` | Form chọn vị trí, cấp độ, loại công ty |
| S04 | Cài đặt: đã bật Google Drive | `#/settings` | Thời điểm đồng bộ gần nhất, nút Đồng bộ ngay và Tắt đồng bộ |

Khi app chạy bên trong Claude, khối Cài đặt AI và Google Drive được ẩn vì AI và dữ liệu do Claude cung cấp.

### S01. Cài đặt: chưa có key
| Desktop | Mobile |
|---|---|
| <img src="screens/s01-settings-desktop.png" width="640"> | <img src="screens/s01-settings-mobile.png" width="240"> |

### S02. Cài đặt: đã lưu key
| Desktop | Mobile |
|---|---|
| <img src="screens/s02-settings-key-saved-desktop.png" width="640"> | <img src="screens/s02-settings-key-saved-mobile.png" width="240"> |

### S03. Cài đặt: sửa mục tiêu học tập
| Desktop | Mobile |
|---|---|
| <img src="screens/s03-settings-edit-goal-desktop.png" width="640"> | <img src="screens/s03-settings-edit-goal-mobile.png" width="240"> |

### S04. Cài đặt: đã bật Google Drive
| Desktop | Mobile |
|---|---|
| <img src="screens/s04-settings-drive-on-desktop.png" width="640"> | <img src="screens/s04-settings-drive-on-mobile.png" width="240"> |

---

## Chụp lại ảnh

Ảnh được chụp tự động bằng Chrome headless, không cần API key. Khi giao diện thay đổi, chạy lại để cập nhật toàn bộ ảnh:

```sh
sh serve.sh                      # mở app ở http://localhost:8000 (để ở một terminal riêng)
python3 tests/shoot_screens.py   # chụp lại vào docs/screens/
python3 tests/shoot_screens.py k01-learn,i07-room-hint   # chỉ chụp một vài màn hình
```

- Dữ liệu mẫu và từng trạng thái được định nghĩa trong [tests/screens.html](../tests/screens.html), ở hai biến `SEED` và `STATES`. Thêm một màn hình mới bằng cách thêm một dòng vào `STATES`, rồi thêm mục tương ứng vào tài liệu này.
- Tên file ảnh có dạng `{mã}-{tên}-desktop.png` và `{mã}-{tên}-mobile.png`. Ảnh mobile chụp ở mật độ điểm ảnh gấp đôi cho sắc nét.
