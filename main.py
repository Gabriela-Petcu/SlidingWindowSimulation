from protocol import run_simulation

if __name__ == "__main__":
    TOTAL_FRAMES = 6
    WINDOW_SIZE = 3
    LOSS_PROBABILITY = 0.25  #25% sanse sa se piarda un frame
    TIMEOUT_INTERVAL = 3     #"secunde" simulate

    run_simulation(
        total_frames=TOTAL_FRAMES,
        window_size=WINDOW_SIZE,
        loss_probability=LOSS_PROBABILITY,
        timeout_interval=TIMEOUT_INTERVAL
    )
