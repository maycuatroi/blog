Viết Một bài blog để chia sẻ về cách implement backup module một cách hiệu quả, lấy ví dụ với bigquery. Tôi đang muốn tạo dung hình ảnh là một AI System Architecture.
Bài viết story telling một cách lôi cuốn người Nghe, cung cấp giá trị cho người đọc.

## Story:
Tôi đã xây dựng một hệ thống tối ưu hóa với dữ liệu lớn. Khi go production thì phát sinh một requirement là với mỗi session chạy.
Với suy nghĩ rất ngây thơ khi đó thì tôi chỉ nghĩ rằng user đang chỉ muốn nhắc tới backup ngắn hạn để chạy lại một số session gần đây phòng trường hợp lỗi hệ thống hoặc có những down-time không mong muốn thì có thể recovery, tôi đã dự định đề xuất sử dung trực tiếp time-travel của Bigquery. Tôi đã chuẩn bị một tài liệu và nghiên cứu giải pháp với bigquery này, giá cả ok, giải pháp backup và recovery hoàn hảo.
  Cho đến ngày họp, biz user trình bày một hồi, và đưa ra mong muốn backup *ít nhất* là 2 năm ... thôi xong, toi. Thôi lệch bài rồi, biết là toi nhưng đến lượt mình thì tôi vẫn lôi slide ra nói một hồi ... chắc chẳng ai hiểu, mình cũng bảo giải pháp này đang backup được tầm 6 tháng (thực ra là 7 ngày). Rồi nhận bài tập của các team, mang về nghĩ dần. Nhưng từ buổi họp đó cũng nắm ra được mấy points:

 Mỗi ngày có hơn 500 session chạy (cho nhiều quốc gia), yêu cầu khi này là cần lưu lại toàn bộ dữ liệu của mỗi session chạy để có thể phân tích, từ đó giải thích về kết quả nếu có thắc mắc và yêu cầu giải thích từ end-user (việc này không thể tránh khỏi khi chúng ta apply giải pháp vào industry). Và quan trọng nhất là dữ liệu này giúp chúng ta có thể thực hiện back-test nhằm đánh giá hiệu quả của những những impact trong quá trình improve hệ thống, khi này với mỗi phiên bản, chúng ta cần đánh giá độ chính xác của AI model/Giải pháp trên những session đã chạy, xem sự sai khác và thay đổi như nào, từ đó có thể *thông báo cho người dùng về những thay đổi có thể sảy ra, mọi impact có thể sảy ra tới bussiness cần được tính toán vầ giải thích.*

Khi này vấn đề nảy sinh là gì ?
1. Data mỗi session rất lớn, nhưng có nhiều sự chùng lặp
2. Data backup storage sao cho hiệu quả về mặt chi phí cũng như tốc độ
3. Rollback không bị chờ quá lâu.

Có 3 cách backup mà tôi muốn nhắc tới trong bài:
1. full backup
2. Incremental backup
3. Differential backup.

## Kiến trúc của backup:

Với kiến trúc hệ thống tôi tạm chia ra làm 5 dataset, lý do chia làm 5 dataset này tôi sẽ viết trong một bài viết khác, đây cũng là một kiến trúc mà tôi khuyến nghị các giải pháp nên áp dụng:
1. Data source
2. Landing dataset
3. Processing layer datasets
4. Result dataset
5. Backup dataset.


Ở bài này chúng ta sẽ đi sâu hơn vào Landing dataset và Backup dataset.

Context:
Data source từ nhiều nguồn với mỗi session sẽ được tập trung toàn bộ ở Landing dataset.
Backup dataset sẽ chia làm 3 phần:
- Head tables
- History tables
- Cold History Storage.