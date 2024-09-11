Main topic: How to grow an Engineering mindset

Bức tranh: Quick and dirty + Science + Solve real world problem + Empathy

- Quick and dirty + science = Drug cooker
- Quick and dirty + solve real world problem = Hit man
- Science + solve real world problem = Noben archiment
- Empathy + solve real world problem = psychiatrist
- Empathy + dirty = Beer 
- Quick and dirty + science + solve real world problem + Empathy = True Engineer

Với xuất thân từ software engineering, tôi đã được học và một phần hiểu sâu sắc về thế nào là software. Từ mindset đó, cuối năm 2016 2017 tôi đã có cơ hội tham gia cuộc thi cuộc đua số với FPT, khi đó lần đầu tiên mình được tiếp xúc với AI. Khi đó còn học chập chững từ những concept đầu tiên là Tensorflow, SSD, Yolo. Thật vậy, mình nghĩ giống với 80% các bạn ngồi đây, mình cũng làm 1 bước vào deep learning, bỏ qua machien learning ban đầu.
Code chạy vù vù, FPS cao, độ chính xác cao, phóng nhanh, đạt giải nhưng đếch hiểu gì. Hòi đấy điếc không sợ súng còn làm cái trò là train model = tensorflow. Xong convert cái model weights sang C++ vì hồi đáy chạy trên con jetson TK1, nên phải convert weights xong rồi chạy với C++ luôn. Vì hồi đấy không nghĩ nó khó nên cứ làm và nó chạy được. -> Quick and dirty

Cơ duyên chặng tiếp theo là gì
Từ giải của cuộc đua số, mình có tí mác thì cũng xin vào Fsoft thực tập luôn. Hồi đó mình phỏng vấn vào Fsoft thì vui lắm, vào cả phòng hội trường to, hỏi có ai Làm AI không, có 2 người giơ tay. Mình với một bạn nữa, hồi đấy là Chiến. Lôi vào phỏng vấn thì hỏi câu gì ? Hỏi mấy câu openCV, xử lý ảnh cơ bản... (Không khó như anh hỏi mấy đứa bây giờ đâu) Chắc hồi đấy nó thế.

Xong mình vào Fsoft từ đó, dự án đầu tiên là dựng hệ thống thí nghiệm người lái cho ô tô, kiểm tra xem người lái xe khi đi trên đường sẽ chú ý vào cái gì. Cơ bản là dùng mask RCNN và PSP Net rồi segment các object, map với toạ độ cái eye gaze của người lái xe để xác định người lái xe đang nhìn vào cái gì. Rồi khi đó đã làm những mô hình Generative rồi, nhưng hồi đấy là thuật toán Genetic Algorithm và reinforcement để tạo ra cái bản vẽ kiến trúc tự động, đảm bảo mấy cái điều kiện. Làm kiểu nghiên cứu, kiểu rất là science luôn. Ai cũng trầm trồ ... nhưng science quá thì không ai dùng được. Lúc đó mình làm khoảng chục dự án kiểu như vậy, làm ra không ai dùng, chỉ là kiểu prototype rồi thử nghiệm mô hình. 

Cho đến một ngày, sau khoảng 2 năm, bài toán đầu tiên mà họ contact tới một đơn vị làm mobile. Thì họ muốn một cái giải pháp khi đó là bài AI on-device đầu tiên của Fsoft. 
Trước giờ các anh em toàn làm về python, mấy cái ngôn ngữ khác và mobile thì sợ lắm. Xong leader trực tiếp của mình khi đó kéo mình ra ngoài nói chuyện riêng là vụ này không nên làm, rủi ro quá nhưng mình cũng bảo là nếu chưa đến mức lỗ thì anh để em làm, em cố được.

- Bài toán khi đó chạy cái AI model trên cái Iphone 8 là cực kỳ khó. Phải convert cái model xử lý ảnh lên mobile và code lại cái module xử lý ảnh opencv với Native C++ của IOS.
- Techstack khi đó khá khủng: C# - Samarin, swift, native c++, python, tensorflow-lite. Việc training model chỉ chiếm đâu đó khoảng 50%.
- Bài toán là dùng AI model, segment cái móng tay người dùng, sau đó replace cái sticker móng tay vào để người dùng có thể connect với máy in để in cái sticker đó ra rồi dán vào móng. Dự án AI đầu tiên go production là lên App Store.

=> Đến khi đó mình mới có cảm nhận về Solve real world problem. Tuy bé nhưng thừa thắng xông lên 

Bigger and more
Xong từ những cơ hội đó mình tiếp bước được những cơ hội lớn hơn là làm PO sản phẩm, xây những hệ thống data management với lượng user lớn hơn, thử thách hơn.


Cuối và đến hôm nay, các dự án cũng khá lớn. Ngoài ra mình cũng đang tư vấn chiến lược chuyển đổi AI cho một số doanh nghiệp SME.

