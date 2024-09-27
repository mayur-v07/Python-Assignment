{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e5499aac-0e42-4001-923a-a650f358f7cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Age :  25\n",
      "Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. Months\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your age is 300.0 Months\n"
     ]
    }
   ],
   "source": [
    "age = float(input(\"Enter your Age : \"))\n",
    "unit = input(\"Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds.\")\n",
    "\n",
    "def survival_duration(age):\n",
    "\n",
    "    months = age*12\n",
    "    weeks = age*52\n",
    "    days = age*365\n",
    "    hours = age*365*24\n",
    "    mins = age*365*24*60\n",
    "    secs = age*365*24*3600\n",
    "    \n",
    "    if unit == 'Months':\n",
    "        print(f\"Your age is {months} Months\")\n",
    "    \n",
    "    elif unit == 'Weeks':\n",
    "        print(f\"Your age is {weeks} Weeks\")\n",
    "    \n",
    "    elif unit == 'Days':\n",
    "        print(f\"Your age is {days} Days\")\n",
    "    \n",
    "    elif unit == 'Hours':\n",
    "        print(f\"Your age is {hours} Hours\")\n",
    "    \n",
    "    elif unit == 'Minutes':\n",
    "        print(f\"Your age is {mins} Minutes\")\n",
    "    \n",
    "    elif unit == 'Seconds':\n",
    "        print(f\"Your age is {secs} Seconds\")\n",
    "    \n",
    "    else:\n",
    "        print(\"Please enter Valid Data\")\n",
    "\n",
    "survival_duration(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5757c43f-8ef7-41a3-8c06-f16205df07e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5012b6b9-e498-46e1-af8a-ea431fde887f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a559f92-4607-4753-93b5-245d25eda9da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8da1084-b5a5-469a-9a04-aa4d04d8a7be",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
