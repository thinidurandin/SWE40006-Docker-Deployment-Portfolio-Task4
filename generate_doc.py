import docx
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

doc = docx.Document()

# Styles
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

# Title
title = doc.add_heading('Deployment Portfolio Task 4 Report', 0)
title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

# Header Details
doc.add_paragraph('Student Name: [Your Name Here]').bold = True
doc.add_paragraph('Student ID: [Your Student ID Here]').bold = True
doc.add_paragraph('Unit Code & Title: SWE40006 Software Deployment and Evolution').bold = True
doc.add_paragraph('Semester & Submission Date: [Current Semester], [Today\'s Date]').bold = True
doc.add_paragraph('Declared Target Level: High Distinction (Task 4.4)').bold = True

doc.add_paragraph('_' * 50)

# Section 1
doc.add_heading('1. Task 4.1: Pass Level - Docker Environment Setup', level=1)
doc.add_heading('Technical Explanation:', level=2)
doc.add_paragraph('To begin the assignment, Docker Desktop was installed on the host Windows machine and a Docker Hub account (kalharad) was registered. To verify the runtime environment was operational, the official hello-world image was pulled and executed.')

doc.add_heading('Execution Evidence:', level=2)
p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the `docker run hello-world` terminal output here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 1: Successful execution of the hello-world container demonstrating an operational Docker environment.').italic = True

doc.add_paragraph('_' * 50)

# Section 2
doc.add_heading('2. Task 4.2 & 4.3: Credit & Distinction Level - Web Application Deployment', level=1)
doc.add_heading('Technical Explanation:', level=2)
doc.add_paragraph('A basic Python web application was engineered using the Flask framework. The application was designed to listen on port 5000 and read an environment variable (ENVIRONMENT) to dynamically adjust its configuration.')
doc.add_paragraph('A custom Dockerfile was written to package the application. It uses the python:3.9-slim base image, installs dependencies from requirements.txt, copies the application files, exposes port 5000, and sets a default environment variable.')
doc.add_paragraph('The container was built locally and deployed using port mapping (-p 8080:5000), allowing host access. Following local verification, the image was pushed to the public Docker Hub repository (kalharad/my-web-app:v1).')
doc.add_paragraph('To verify multi-host capability and public accessibility (HTTP/HTTPS), the image was pulled and executed on a secondary Docker environment (Killercoda Ubuntu Playground).')

doc.add_heading('Local Deployment Evidence:', level=2)
p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the local docker build and docker run terminal output here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 2: CLI output showing the successful local build and execution of the web application.').italic = True

p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the web browser at localhost:8080 here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 3: Web browser confirming local access and environment variable injection.').italic = True

doc.add_heading('Docker Hub Push Evidence:', level=2)
p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the docker push terminal output here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 4: Pushing the compiled container image to the public Docker Hub registry.').italic = True

doc.add_heading('Multi-Host & Public Accessibility Evidence (Killercoda):', level=2)
p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the Killercoda terminal here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 5: Pulling and running the container on a secondary Docker host environment.').italic = True

p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the public webpage accessed via Killercoda here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 6: Verifying public HTTP accessibility of the web application over the internet.').italic = True

doc.add_paragraph('_' * 50)

# Section 3
doc.add_heading('3. Task 4.4: High Distinction Level - Non-Web Service & Volume Orchestration', level=1)
doc.add_heading('Technical Explanation:', level=2)
doc.add_paragraph('For the non-web service component, a Python data processing script (processor.py) was developed. This script is designed to read an input text file, calculate the total word and character counts, simulate processing time, and write the results to an output file.')
doc.add_paragraph('A separate Dockerfile was created to package this CLI tool. To handle persistent volume storage, the container was executed using a host mount (-v). This allowed the container to read input.txt from the host\'s data directory and write output.txt back to the host, demonstrating container lifecycle execution and persistent state management without a web server.')

doc.add_heading('Execution Evidence:', level=2)
p = doc.add_paragraph()
p.add_run('*(Paste your screenshot of the terminal running the docker run -v ... command here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 7: Container orchestration executing the CLI application with persistent host volume mounts.').italic = True

p = doc.add_paragraph()
p.add_run('*(Paste your screenshot showing the output.txt file generated on your Windows machine here)*').italic = True
p = doc.add_paragraph()
p.add_run('Figure 8: Verification of persistent storage; the generated output file successfully written to the host filesystem.').italic = True

doc.add_paragraph('_' * 50)

# Section 4
doc.add_heading('4. External Code & Script Repository', level=1)
doc.add_paragraph('All application source code, initialization scripts, and Dockerfiles used in this deployment portfolio have been version-controlled and are publicly accessible at the following repository:')

p = doc.add_paragraph()
p.add_run('GitHub Repository URL: [Paste your GitHub Repository Link Here]').bold = True
p = doc.add_paragraph()
p.add_run('*(Note: No sensitive credentials or raw binaries are included in the repository).*').italic = True

doc.save('Report_Template.docx')
print("Successfully generated Report_Template.docx")
