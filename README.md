# Hello Jesse.

Jesses this is a README file for source control repostiory. You can see information about the code here if someone takes the time to write one.

These files have a special language called **markdown**. Markdown is merely a way to style the words. For example, you'll notice I bolded the word *markdown* I did this by wrapping the word markdown with two asterisks (**). You'll notice the word above is italicized. I did that using only a single asterisk. You can see the syntax simply by opejing this file in a text editor. 

BUT NOTICE! GitHub interprets the styles. 

Use Markdown files to document what your code does!


## Installing dotnet Core on Raspian (Raspberry Pi).

1. Open a terminal
2. Become root in your terminal by typing the below command. root is the admin account on MOST linux systems. 

    ```
    sudo -i
    ```
3. Run updates on your Pi by executing the following command in your terminal
   
   ```
   apt-get update

   # Then install dependencies
   apt-get install curl libunwind8 gettext apt-transport-https
   ```
   *note: Notice that I used the # sign in the code block above before a line of code. This is a comment. They are not interpreted by code and are there for information purposes. You can write anything after comments!*

4. Sign-out of your current root session by typing `exit` in your console and hitting enter. We want to install dotnet as a non-admin.

5. Then run the following command line to actually install the SDK.
   
   ```
   curl -sSL https://dot.net/v1/dotnet-install.sh | bash
   ```

6. The final step is to add a few variables into some linux files. This allows the operating system to understand WHERE to look for certain dotnet tools.

   ```
   export DOTNET_ROOT=$HOME/.dotnet
   echo PATH=$PATH:$DOTNET_ROOT:$DOTNET_ROOT/tools >> $HOME/.bashrc
   ```
   *The above commands set a variable using the `export` command. Then use that variable and `echo` (or print) it to a file using the `>>` operator. Using double `>>` means APPEND to the file the value to the right of the `echo`  statement (`PATH=$PATH:$DOTNET_ROOT:$DOTNET_ROOT/tools`) is now at the bottom of the `$HOME/.bashrc` file.*

7. To verify the dotnet installtion worked run the below command.


   ```
   dotnet --version
   ```
   If you see a version string printed out, everything is working as expected.


## Creating your first dotnet program 

Let's make you into a neckbeard. I want us to remain in the commandline. You will notice the use of the `$HOME` variable. This is a variable in linux that references your home directory. This is just like on Windows when you have your `Documents` directory. To enter this directory use the `cd` command. `cd` in linux is change directory. In our case we want to go `$HOME`. But what exactly in `$HOME`?

`$HOME` is merely a reference to a directory. Even more low level, it's just text. So let's see what `$HOME` actually equals. To do this, type the below command
```
echo $HOME
```
If this is successful you should see something like `/home/pi` or whatever your username is (not pi). For the rest of this tutorial, we will ASSUME your username is `pi`.

Ok now that we have that out of the way lets use this variable. Let's go to your home directory by using the `cd` command mentioned above. Type the below.

```
cd $HOME
```
This command IS ALSO THE SAME as if you typed `cd /home/pi`. variables make your life easier!

Let's learn one more quick command. Let's verify you are in your `$HOME` directory. Type `pwd` and hit enter. `pwd` is a command that stands for **P**rint **W**orking **D**irectory. It shows whatever directory you're in. This should equal whatever your `$HOME` variable equals.

Ok now let's create a directory where we can store our code. Run `mkdir src`.
This `mkdir` makes a directory called `src`. I like to store all my projects in a folder called `src` (source). 

Now go into that directory. 
```
cd src/
```

Let's create one more directory and enter into it.
```
mkdir myfirstdotnet
cd myfirstdotnet
```

Alright. The final step creating your dotnet project. Run the below command.
```
dotnet new console
```

If everything is successful you should see the below words.

    The template "Console App" was created successfully.

Now let's make sure it runs!! Run the following command.
```
dotnet run
```

If successful, you should see 
    
    Hello, World

Happy coding!





