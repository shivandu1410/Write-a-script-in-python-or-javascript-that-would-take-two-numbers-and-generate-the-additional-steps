import json

def generate_steps(num1, num2):
    carry = 0
    steps = {}
    for i in range(max(len(str(num1)), len(str(num2)))):
        n1 = int(str(num1)[-i-1]) if i < len(str(num1)) else 0
        n2 = int(str(num2)[-i-1]) if i < len(str(num2)) else 0
        s = n1 + n2 + carry
        carry = s // 10
        steps[f"step{i+1}"] = {"carryString": "1" * carry, "sumString": str(s)[-1]}
    return json.dumps(steps, indent=4)

num1 = 1489
num2 = 714

steps_json = generate_steps(num1, num2)
print(steps_json)
