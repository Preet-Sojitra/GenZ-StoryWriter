import time

dummy_story = """
Title: The Cartoon Character's Brushing Adventure

FADE IN:

INT. CARTOON CHARACTER'S ROOM - DAY

A cartoon character, wearing a hat and holding a toothbrush, stands in front of a mirror. He looks at himself in the mirror and starts brushing his teeth.

CARTOON CHARACTER (V.O.) Morning! Time to start my brushing adventure!

The cartoon character continues brushing his teeth for a few seconds, then suddenly stops and looks surprised. He puts down the toothbrush and turns to the camera.

CARTOON CHARACTER (V.O.) Oh no! My hat has fallen off!

He quickly reaches out and picks up the hat from the floor.

CARTOON CHARACTER (CONT'D) No problem! I'll just put this hat back on.

The cartoon character puts on the hat and continues brushing his teeth, this time with more care. He finishes brushing and turns to the camera once again.

CARTOON CHARACTER (V.O.) And that was my brushing adventure! Time to go out and have some fun!

FADE OUT.
"""

"""
    This is a mock story generator. It tries to replicate the behaviour of the mistral model. It returns a dummy story after a delay of 8 seconds. Since the mistral model takes much time to generate the story, we are using the mock story generator to replicate the behaviour of the mistral model for testing purposes.
"""


def call_model(prompt):
    # return after some amount of delay. As in real life, the model will take some time to generate the story
    time.sleep(8)
    return dummy_story


dummy_story_2 = """
Title: "Chasing Dreams"

FADE IN:

EXT. PARK - DAY

A little boy, JASON, stands on a grass field, holding a frisbee in his hand. He looks up at the sky with a determined look on his face.

JASON (V.O.) I want to be the best player in the world.

He throws the frisbee high into the air and catches it with one hand, then runs towards the goal post, slamming the disc through it. He jumps up, looking at his progress with pride.

JASON (V.O.) But first, I have to prove myself.

He continues to play, facing off against other kids in the park, each time getting better and more confident.

CUT TO:

INT. COACH'S OFFICE - DAY

Coach Johnson watches Jason's game from behind a desk, taking notes on a clipboard. He gets up and approaches him.

COACH JOHNSON You have potential, kid. But you need to work harder.

Jason nods, determined to take the coach's advice to heart.

CUT TO:

EXT. PARK - DAY

Jason practices every day, perfecting his throws and learning new techniques from his coach. He becomes known as the best player in the park, drawing crowds of kids to watch him play.

CUT TO:

INT. COACH'S OFFICE - DAY

Coach Johnson watches Jason practice, a proud smile on his face.

COACH JOHNSON You're a natural, kid. But don't get complacent. Keep pushing yourself.

Jason nods, taking the coach's words to heart. He continues to work hard and improve his skills.

CUT TO:

EXT. PARK - DAY

Months have passed, and Jason has become a skilled frisbee player, able to perform tricks and stunts that leave other players in awe. He competes in tournaments and wins first place every time.

CUT TO:

INT. COACH'S OFFICE - DAY

Coach Johnson watches Jason play on TV, cheering him on.

COACH JOHNSON
"""
