import random

from config import hearts, heart_matrix

async def generate_heart():
    heart_output = "\n".join(
        "".join(
            random.choice(hearts) 
            if cell == 1 else "❤️" 
            for cell in row)
        for row in heart_matrix)

    return heart_output