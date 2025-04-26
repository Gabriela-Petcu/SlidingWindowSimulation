import random

def should_lose_frame(probability: float) -> bool:
    """

    -decide daca un cadru trb sa fie pierdut in timpul trnasmisiei
    Param:
    -probability(float): probabilitatea ca un cadru sa fie pierdut(0 sau 1)
    Return:
    -bool:true daca se pierde, false daca este transmis cu succes
    """
    return random.random() < probability

def display_state(step: int, sender_window, acks_received, receiver_buffer):
    """
    -starea curenta a simularii la fiecare pas
    Param:
    -step(int): nr pasului curent din simulare
    -sender_window(list):lista cadrelor aflate in fereastra senderului
    -acks_received(set): multimea cadrelor confirmate(ack-uri primite)
    -receiver_buffer(dict): dictionar cu cadrele receptionate(cheie=nr cadru, valoare=nr cadru)
    """
    print(f"\n--- PASUL {step} ---")
    print(f"Sender window: {sender_window}")
    print(f"ACK-uri primite: {sorted(acks_received)}")
    print(f"Cadre primite de receiver (nesortate): {list(receiver_buffer.values())}")

def print_final_state(receiver_buffer):
    """
    -rezultatul final al simularii: ordinea in care au fost receptionale cadrele,lista acestora sortata
    """
    print("\n--- TRANSMISIA S-A TERMINAT ---")
    print(f"Cadre primite (in ordinea primirii): {list(receiver_buffer.values())}")
    print(f"Cadre primite (sortate): {sorted(receiver_buffer.values())}")
