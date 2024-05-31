from core.generator import image_generation
from core.working_with_files import write_image_data


exercise = "Для учебника по математике, мультфильм."
prompt = "Два весёлых строителя на стройке."

image_data = image_generation(prompt, exercise)

write_image_data(image_data, prompt)
