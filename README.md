Copyright (C) Himabindu Boddupalli and Prachi Patwardhan.

	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    	
	Contact Us:
	himabindu.bs@gmail.com
	prachipatwardhan1@gmail.com
	     
*************************************************************************/

Working:
This project downloads the top 10 songs in the Billboard's Hot-100
list automatically every week. 

Scripts Used:
This project is written in Python, HTML, CSS, Javascript.

Contents:
Part1:
	Website which allows you to automatically download the top 10 songs off of Billboard each week.
	It also allows you to download an individual song from youtube given the song name and artist name.

Part2:
	Additional tool that allows you to download any individual song, to be run via command line.


Prerequisites:
You must have the following modules installed (for your version of Python)in order to use the software-
1)Pafy
2)Requests
3)BeautifulSoup
4)Youtube-dl

Setting Up:
This works on localhost. A local server will be required to run it. Steps to be taken for the same:
1. Install XAMPP server, which is available for Linux, Windows and Mac
2. Ensure that Apache2 is configured to run Python scripts as CGI. This will require changing the permissions and the configuration of Apache2.
3. Install the required modules, depending on which version of Python is being used. These can be easily downloaded using pip.
4. Ensure that all of the required files for the application are in the folder for the server.
5. The crontab file and shell script should be edited according to the directory and started as a crontab job.
	*crontab crontab.txt*


WORD OF CAUTION: Please do not distribute it without the author's permission.
