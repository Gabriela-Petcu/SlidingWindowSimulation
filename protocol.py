from utils import should_lose_frame, display_state, print_final_state

def run_simulation(total_frames, window_size, loss_probability, timeout_interval):
    """
    -simuleaza protocolul pt transmiterea de cadre cu pierderi
    Param:
    -total_frames(int): nr total de cadre care trb transmise
    -window_size(int): dim ferestrei glisante a senderului
    -loss_probability(float): probabilitatea de pierdere a unui frame
    -timeout_interval(int): nr de pasi de timp dupa care un frame se retransmite daca nu a primit ack


    """
    frames_to_send = list(range(1, total_frames + 1))
    sender_window = []                 # cadre aflate in fereastra
    receiver_buffer = {}              # cadre primite (chiar si in afara ordinii)
    acks_received = set()             # ACK-uri primite
    sent_timestamps = {}              # momentul simulat in care a fost trimis fiecare cadru
    next_frame_to_send = 0            # urmatorul cadru de trimis
    step = 0                          # "timpul" simulat
    sender_base = 0                   # inceputul ferestrei (pentru logica glisarii)

    while len(acks_received) < total_frames:
        #trimitem cadre noi daca mai e loc in fereastra
        while len(sender_window) < window_size and next_frame_to_send < total_frames:
            frame = frames_to_send[next_frame_to_send]

            if not should_lose_frame(loss_probability):
                print(f"Sender: Sending frame {frame}")
                receiver_buffer[frame] = frame
                print(f"Receiver: Received frame {frame}, sending ACK {frame}")
            else:
                print(f"Sender: Sending frame {frame} -> LOST!")

            sent_timestamps[frame] = step
            sender_window.append(frame)
            next_frame_to_send += 1

        #procesam ack-uri
        for frame in list(sender_window):
            if frame in receiver_buffer:
                acks_received.add(frame)

        #daca ack-ul pt primul frame din fereastra a fost primit se gliseaza fereastra
        while sender_window and sender_window[0] in acks_received:
            print(f"Sender: ACK {sender_window[0]} received, sliding window")
            sender_window.pop(0)

        #verif timeout pt primul frame din fereastra
        if sender_window:
            oldest_frame = sender_window[0]
            if step - sent_timestamps[oldest_frame] >= timeout_interval:
                print(f"Sender: Timeout for frame {oldest_frame}, retransmitting...")

                if not should_lose_frame(loss_probability):
                    print(f"Sender: Retransmitting frame {oldest_frame}")
                    receiver_buffer[oldest_frame] = oldest_frame
                    print(f"Receiver: Received frame {oldest_frame}, sending ACK {oldest_frame}")
                    sent_timestamps[oldest_frame] = step
                else:
                    print(f"Sender: Retransmitting frame {oldest_frame} -> LOST!")

        display_state(step, sender_window, acks_received, receiver_buffer)
        step += 1

    print_final_state(receiver_buffer)
