🪟 SlidingWindowProtocol 🪟
SlidingWindowProtocol is a Python simulation of a reliable data transmission method using a sliding window mechanism, featuring simulated frame loss and timeout-based retransmissions.

📌 Features
🚀 Frame Sending: Send frames in a sliding window fashion to maximize throughput.
❌ Frame Loss Simulation: Frames can randomly be lost based on a configurable probability.
⏰ Timeouts & Retransmissions: Frames are resent if not acknowledged within the timeout interval.
📈 Dynamic Window Management: The sender slides its window based on received acknowledgments.
📬 Receiver Buffering: Frames are buffered and confirmed even when received out of order.

🛠️ Technologies Used
Python 3.x – Main programming language.
Random module – For simulating unpredictable network conditions.
Simple Simulation Framework – No external libraries required.

🎮 How It Works
Set parameters: total frames, window size, frame loss probability, and timeout interval.
Start simulation and observe frame transmissions, losses, ACK receptions, and retransmissions.
The simulation continues until all frames are successfully received and acknowledged.

🚀 Setup & Running
1. Clone the repository:
git clone https://github.com/your-username/SlidingWindowProtocol.git
cd SlidingWindowProtocol
2. Run the simulation:
python main.py
