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

dummy_story_2 = """
Title: Beyond the Fence
INT. WOODEN FENCE - NIGHT
A young girl named LUCY is sitting in her tent, looking out at the stars through a small hole in the
roof. She is lost in thought, dreaming of adventure beyond the wooden fence that surrounds her
family's property. Suddenly, she hears the sound of hooves approaching and turns to see a pair of
horses running across the dirt field towards her.
EXT. DIRT FIELD - NIGHT
The horses come to a stop in front of Lucy's tent and the girl cautiously approaches them. She
reaches out a hand and one of the horses nuzzles it, allowing her to stroke its mane. Lucy is filled
with excitement as she realizes that this could be the beginning of an adventure beyond the fence.
INT. TENT - NIGHT
Lucy quickly packs a small bag with some supplies and climbs onto the back of one of the horses.
The other horse follows suit and the two set off into the night, galloping across the fields. Lucy is
filled with joy as she feels the wind in her hair and the thrill of being free from the confines of her
wooden fence.
EXT. FIELD - NIGHT
As they ride further and further away from home, Lucy can't help but feel a sense of freedom and
possibility that she has never experienced before. She is filled with wonder at what lies beyond the
fence and what adventures await her in the world outside. The horses continue to run, carrying Lucy
on their backs towards an unknown future.
FADE OUT
"""


"""
    This is a mock story generator. It tries to replicate the behaviour of the mistral model. It returns a dummy story after a delay of 8 seconds. Since the mistral model takes much time to generate the story, we are using the mock story generator to replicate the behaviour of the mistral model for testing purposes.
"""


def call_model(prompt):
    # return after some amount of delay. As in real life, the model will take some time to generate the story
    time.sleep(8)
    return dummy_story_2
