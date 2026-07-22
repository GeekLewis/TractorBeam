"""
Dual Analog Stick Mover
------------------------
Requires: pygame-ce  (pip install pygame-ce)

- Left stick moves the YELLOW SQUARE
- Right stick moves the ORANGE CIRCLE
- Raw + smoothed axis values are printed at the top of the window
- Works on Mac or Windows with any SDL-recognized gamepad (Xbox, PS, etc.)

Note on axis numbering:
Most controllers report axes in this order via SDL/pygame:
    0 = Left Stick X
    1 = Left Stick Y
    2 = Right Stick X
    3 = Right Stick Y
(Triggers, if present, usually show up as axes 4/5.)
If your controller maps differently, the on-screen "Raw axes" list at the
bottom will show you every axis index and its live value so you can adjust
LEFT_X_AXIS / LEFT_Y_AXIS / RIGHT_X_AXIS / RIGHT_Y_AXIS below.
"""

import sys
import pygame

# ----------------------------- Config ---------------------------------

SCREEN_W, SCREEN_H = 800, 600
BG_COLOR = (0, 0, 0)
SQUARE_COLOR = (255, 255, 0)     # yellow
CIRCLE_COLOR = (255, 140, 0)     # orange

OBJ_SIZE = 12            # square is OBJ_SIZE x OBJ_SIZE, circle diameter = OBJ_SIZE
SPEED = 500.0            # pixels per second at full stick deflection
DEADZONE = 0.12          # ignore small stick noise below this magnitude

# Default axis indices (typical Xbox/PS layout under SDL)
LEFT_X_AXIS = 0
LEFT_Y_AXIS = 1
RIGHT_X_AXIS = 2
RIGHT_Y_AXIS = 3

# -------------------------------------------------------------------


def apply_deadzone(value, deadzone):
    if abs(value) < deadzone:
        return 0.0
    # rescale so output still reaches 1.0 at full deflection
    sign = 1.0 if value > 0 else -1.0
    scaled = (abs(value) - deadzone) / (1.0 - deadzone)
    return sign * scaled


def clamp(value, lo, hi):
    return max(lo, min(hi, value))


def main():
    pygame.init()
    pygame.joystick.init()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Dual Stick Mover (pygame-ce)")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("consolas", 20)
    small_font = pygame.font.SysFont("consolas", 16)

    joystick = None
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Connected controller: {joystick.get_name()} "
              f"({joystick.get_numaxes()} axes)")
    else:
        print("No controller detected. Plug one in and restart.")

    # Start both objects centered, offset slightly so they don't overlap
    square_pos = [SCREEN_W / 2 - 60, SCREEN_H / 2]
    circle_pos = [SCREEN_W / 2 + 60, SCREEN_H / 2]

    half = OBJ_SIZE / 2

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.JOYDEVICEADDED:
                joystick = pygame.joystick.Joystick(event.device_index)
                joystick.init()
                print(f"Connected controller: {joystick.get_name()}")
            elif event.type == pygame.JOYDEVICEREMOVED:
                print("Controller disconnected.")
                joystick = None

        raw_lx = raw_ly = raw_rx = raw_ry = 0.0
        lx = ly = rx = ry = 0.0
        num_axes = 0

        if joystick is not None:
            num_axes = joystick.get_numaxes()
            if num_axes > LEFT_X_AXIS:
                raw_lx = joystick.get_axis(LEFT_X_AXIS)
            if num_axes > LEFT_Y_AXIS:
                raw_ly = joystick.get_axis(LEFT_Y_AXIS)
            if num_axes > RIGHT_X_AXIS:
                raw_rx = joystick.get_axis(RIGHT_X_AXIS)
            if num_axes > RIGHT_Y_AXIS:
                raw_ry = joystick.get_axis(RIGHT_Y_AXIS)

            lx = apply_deadzone(raw_lx, DEADZONE)
            ly = apply_deadzone(raw_ly, DEADZONE)
            rx = apply_deadzone(raw_rx, DEADZONE)
            ry = apply_deadzone(raw_ry, DEADZONE)

        # Move objects
        square_pos[0] += lx * SPEED * dt
        square_pos[1] += ly * SPEED * dt
        circle_pos[0] += rx * SPEED * dt
        circle_pos[1] += ry * SPEED * dt

        # Keep on screen
        square_pos[0] = clamp(square_pos[0], half, SCREEN_W - half)
        square_pos[1] = clamp(square_pos[1], half, SCREEN_H - half)
        circle_pos[0] = clamp(circle_pos[0], half, SCREEN_W - half)
        circle_pos[1] = clamp(circle_pos[1], half, SCREEN_H - half)

        # --------------------------- Draw ---------------------------
        screen.fill(BG_COLOR)

        pygame.draw.aaline(screen, "yellow", square_pos, circle_pos, 3)
        square_rect = pygame.Rect(0, 0, OBJ_SIZE, OBJ_SIZE)
        square_rect.center = (round(square_pos[0]), round(square_pos[1]))
        pygame.draw.rect(screen, SQUARE_COLOR, square_rect)

        pygame.draw.circle(
            screen, CIRCLE_COLOR,
            (round(circle_pos[0]), round(circle_pos[1])),
            OBJ_SIZE // 2
        )

        # ------------------------ HUD text ---------------------------
        lines = [
            f"Left stick  (square) -> X: {lx:+.3f}  Y: {ly:+.3f}"
            f"   raw X: {raw_lx:+.3f}  raw Y: {raw_ly:+.3f}",
            f"Right stick (circle) -> X: {rx:+.3f}  Y: {ry:+.3f}"
            f"   raw X: {raw_rx:+.3f}  raw Y: {raw_ry:+.3f}",
        ]
        if joystick is None:
            lines.append("No controller connected")

        y = 10
        for line in lines:
            surf = font.render(line, True, (255, 255, 255))
            screen.blit(surf, (10, y))
            y += surf.get_height() + 4

        # Optional: list every raw axis on the controller, for remapping help
        if joystick is not None and num_axes:
            axis_str = "  ".join(
                f"a{i}:{joystick.get_axis(i):+.2f}" for i in range(num_axes)
            )
            axis_surf = small_font.render(
                f"Raw axes: {axis_str}", True, (150, 150, 150)
            )
            screen.blit(axis_surf, (10, SCREEN_H - axis_surf.get_height() - 8))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()