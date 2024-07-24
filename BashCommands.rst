.. ########################################################
   #                                                       #
   #               USEFUL LINUX BASH COMMANDS              #
   #              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~             #
   #                   Version 0.0.1                       #                
   #                                                       #
   #           ~~~~~~~~~~~~~~~~~~~~~~~~~                   #
   #           | HOST USED FOR EXAMPLES:  * ralice.xyz *   #
   #           ~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~   #
   #                                                       #   
   #                 By: Alexis Leclerc                    #
   #                 Created: 07/23/2024                   #
   #                 Updated: 07/23/2024                   #
   #           DWistled Knows The Current Chapter          #
   ########################################################

SSH: Use Putty SSH Client [Port 22]
User: Alexis
Pass: Toor5access
host used for examples

.. code-block:: text

   #1 pt r
   . X  X 
   . X  X 
   . .  X 
   . .  X 
   . .  X 
   . .  . 
          
   #1apter

=======================================================================================================================================================================
Bash Terminal Commands
=======================================================================================================================================================================

.. ####################################################
   #                File & Filepath Commands           #
   ####################################################

   |---------------------------------------------------- |
   | Show The Current Directory:                         |
   |---------------------------------------------------- |
   
   ls

   |---------------------------------------------------- |
   | Home or root Directory:                             |
   |---------------------------------------------------- |
   
   cd

      OR,

   cd ~/ '~' Represents The Current user's home Directory.

   |---------------------------------------------------- |
   | Change Directory:                                   |
   |---------------------------------------------------- |
   
   Subdirectory of home/:    cd ~/subdirectory/
   ~~~~~~~~~~~~~~~~~~~~~
   
      Any Directory /:    cd /path/to/folder/file.csv
      ~~~~~~~~~~~~~~~

         Example:    cd /usr/lib or cd /home/Alexis
         ~~~~~~~

   |---------------------------------------------------- |
   | Create A New Folder (Directory):                    |
   |---------------------------------------------------- |
   
   mkdir <folder_name>

.. ####################################################
   #             File & Folder Permissions             #
   ####################################################

   | Show The Current Directory:                         |
   |---------------------------------------------------- |
   
   ls

   |---------------------------------------------------- |
   | Home or root Directory:                             |
   |---------------------------------------------------- |
   
   cd

      OR,

   cd ~/ '~' Represents The Current user's home Directory.

   |---------------------------------------------------- |
   | Change Directory:                                   |
   |---------------------------------------------------- |
   
   Subdirectory of home/:    cd ~/subdirectory/
   ~~~~~~~~~~~~~~~~~~~~~
   
      Any Directory /:    cd /path/to/folder/file.csv
      ~~~~~~~~~~~~~~~

         Example:    cd /usr/lib or cd /home/Alexis
         ~~~~~~~

   |---------------------------------------------------- |
   | Create A New Folder (Directory):                    |
   |---------------------------------------------------- |
   
   mkdir <folder_name>

=======================================================================================================================================================================
Running Tasks/Processes
=======================================================================================================================================================================

.. ####################################################
   #                     I/O Priority                  #
   ####################################################

   | Set I/O Priority for a New Process:                |
   |--------------------------------------------------- |
   
   ionice -c <class> -n <priority> command

   | Change I/O Priority of an Existing Process:        |
   |--------------------------------------------------- |
   
   ionice -c <class> -n <priority> -p <PID>
   
   ionice -c 2 -n 0 -p

   <class>: The I/O scheduling class. Options are:
      I)   1 for real-time
      II)  2 for best-effort ***USE
      III) 3 for idle

   <priority>: The priority level. For classes 2 and 3, the priority ranges from 0 (highest) to 7 (lowest).

.. ####################################################
   #                     CPU Priority                  #
   ####################################################
   
   | Start a New Process with a Specific Nice Level:    |
   |--------------------------------------------------- |
   
   nice -n <nice_value> command

   | Change the Nice Level of an Existing Process:      |
   |--------------------------------------------------- |
   
   renice -n <nice_value> -p <PID>
   
   renice -n -20 -p 

   <nice_value>: The CPU Priority. Options are:
      I)   -20 for Highest Priority (Not Nice To Other Tasks)
      II)    0 for Normal  Priority
      III)  20 for Lowest  Priority (Nice To Other Tasks)

.. ####################################################
   #                   Using Both                      #
   ####################################################
   
   | Using Both To Create A New Process and Modify It Process: |
   |---------------------------------------------------------- |
   
   nice -n <nice_value> command
   ionice -c 2 -n 0 -p <PID>

   | Using Both To Create A Modify An Existing Process:        |
   |---------------------------------------------------------- |
   
   renice -n -20 -p 
   ionice -c 2 -n 0 -p 

.. #####################################################
   #        Running A Process In The Background        #
   #####################################################
   
   | Starting A New Screen:                              |
   |---------------------------------------------------- |
   
   screen -S <Session_Name>

   | Kill a Screen Session:                              |
   |---------------------------------------------------- |
   
   exit
   
   screen -X -S <session_id> quit

   | List All Screens:                                   |
   |---------------------------------------------------- |
   
   screen -ls

   | Detach from a Screen Session:                       |
   |---------------------------------------------------- |
   
   screen -r <session_id>
   
   screen -r <session_name>

   | Detach from a Screen Session:                       |
   |---------------------------------------------------- |
   
   Ctrl-a d

=======================================================================================================================================================================
Setting Up Bash Aliases
=======================================================================================================================================================================

.. ####################################################
   #                   Creating Shortcuts              #
   ####################################################

   Step 1:
   cd

   Step 2:
   nano .bashrc

   Step 3:    ADD OR MODIFY:
   -------------------------
   
   alias m='mysql -u root -pAL\@12345'
   alias mvar='mysql -u root -pAL\@12345 Variables'
   alias largepipe='mysql -u root -pAL\@12345 FinalPipe'
   alias vars='cd /home/Alexis/FilesToCreateDatabase/9Variables'
   alias a='cd /home/Alexis'

   Step 4:
   ctrl-x 
   <wait for menu at the bottom of the screen>
   Y
   <Save file with filename (either rename or dont touch it i.e. let it be)>
   *Press ENTER

   Step 5:
   SOURCE/"UPDATE" THE BASH COMMANDS
   ------------------------------------
   
   In Terminal copy paste by right clicking:
   --------------------------------------
   |
   if [ -f /etc/bashrc ]; then
   . /etc/bashrc
   fi
   |
   --------------------------------------

=======================================================================================================================================================================
Automating A Bash Script
=======================================================================================================================================================================

.. ####################################################
   #                    Using A Batch Script           #
   ####################################################
   
   | Command              | Example                     |
   |----------------------|-----------------------------|
   | chmod +x <file_name>.sh | chmod +x manage_tasks.sh  |
   | ./<file_name>.sh     | ./manage_tasks.sh           |

   This script can be used to:
      1) Login to MySQL with a. No DB selected OR b. Login to Variables DB
      2) Run a python3 script with a selected filepath
      3) Run an R script with a selected filepath

   .. code-block:: bash
   
      #!/bin/bash

      # Function to handle MySQL login
      mysql_login() {
          echo "Choose database option:"
          echo "1) No DB"
          echo "2) Variables DB"
          read -p "Enter choice [1-2]: " db_choice
          
          case $db_choice in
              1)
                  echo "Logging into MySQL with no database..."
                  echo "Enter your custom PID or press Enter to use default:"
                  read custom_pid
                  if [ -z "$custom_pid" ]; then
                      mysql -u root -pAL\@12345
                  else
                      nice -n -20 mysql -u root -pAL\@12345 &
                      pid=$!
                      if [ -n "$custom_pid" ]; then
                          ionice -c 2 -n 0 -p $custom_pid
                      else
                          ionice -c 2 -n 0 -p $pid
                      fi
                  fi
                  ;;
              2)
                  echo "Logging into MySQL with Variables DB..."
                  echo "Enter your custom PID or press Enter to use default:"
                  read custom_pid
                  if [ -z "$custom_pid" ]; then
                      mysql -u root -pAL\@12345 Variables
                  else
                      nice -n -20 mysql -u root -pAL\@12345 Variables &
                      pid=$!
                      if [ -n "$custom_pid" ]; then
                          ionice -c 2 -n 0 -p $custom_pid
                      else
                          ionice -c 2 -n 0 -p $pid
                      fi
                  fi
                  ;;
              *)
                  echo "Invalid choice."
                  ;;
          esac
      }

      # Function to run a Python script
      run_python_script() {
          read -p "Enter the filepath of the Python script: " python_file
          echo "Running Python script..."
          echo "Enter your custom PID or press Enter to use default:"
          read custom_pid
          if [ -z "$custom_pid" ]; then
              python3 $python_file
          else
              nice -n -20 python3 $python_file &
              pid=$!
              if [ -n "$custom_pid" ]; then
                  ionice -c 2 -n 0 -p $custom_pid
              else
                  ionice -c 2 -n 0 -p $pid
              fi
          fi
      }

      # Function to run an R script
      run_r_script() {
          read -p "Enter the filepath of the R script: " r_file
          echo "Running R script..."
          echo "Enter your custom PID or press Enter to use default:"
          read custom_pid
          if [ -z "$custom_pid" ]; then
              Rscript $r_file
          else
              nice -n -20 Rscript $r_file &
              pid=$!
              if [ -n "$custom_pid" ]; then
                  ionice -c 2 -n 0 -p $custom_pid
              else
                  ionice -c 2 -n 0 -p $pid
              fi
          fi
      }

      # Main script
      echo "Choose an action:"
      echo "1) Login to MySQL"
      echo "2) Run Python script"
      echo "3) Run R script"
      read -p "Enter choice [1-3]: " choice

      case $choice in
          1)
              mysql_login
              ;;
          2)
              run_python_script
              ;;
          3)
              run_r_script
              ;;
          *)
              echo "Invalid choice."
              ;;
      esac
