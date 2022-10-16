# Pinterest Pin Generator Script

## Description
I had the idea for this project as an attempt to automate the task of generating pins for Pinterest to promote my online t-shirt store. Initially I created many (nearly 80) pin templates in svg (vector) format. But using them to create 5 daily pins with a vector image editor proved to be a very monotonic task. So I decided to  use Python to manipulate my pin templates, so that I could create at once as many pins as I wanted.

I briefly describe the image files and folders the script uses. There is one generic folder containing several subfolders: a _product_images_ folder, with all the pictures I want to promote in Pinterest; a _saved_pins_ folder, where the generated pins are saved; and several _template_nn_ folders, containing each a _bg.png_ image file and a _fg.png_ image file, needed to generate one specific pin model.

!['Folders'](images/folders.png)


To generate one pin, the script takes a (let's call it _pd.png_) image file from the _product_images_ folder, as well as  _bg.png_ and _fg.png_ files (the latter has transparent background) from a template folder. It then pastes all three of them together, one onto the other, to form one single one, which is the final pin. The pin is then saved in the _saved_pins_ folder.

!['Product'](images/template.png)

To generate  _n_ pins, the script randomly chooses _n_ images from the _product_image_ folder and _n_ pin template folders, and uses them to generate _n_ pins. The product image file name and template numbers are written in a _log.txt_ and a _registry.txt_ respectively, so that the script excludes them when generating the next set of pins, avoiding repetition. After eight executios of the script, a previously used template can be chosen again.

!['Pins'](images/pines_generados.png)
