# rackspace_interview_code

pre-requisites:  
  - ensure podman is installed  and up and running in the linux operating system
  - download the rar file and place it an specific directory 
  - ensure both files (Containerfile and rack-bill-code.py) are present in the directory

1) create podman image using following command:
    # podman build . -t code:latest
    
 2) Create the containg using above image for executing 
   #  podman run localhost/code

