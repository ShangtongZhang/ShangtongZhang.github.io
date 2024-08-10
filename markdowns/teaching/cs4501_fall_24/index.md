---
layout: page
title: Reinforcement Learning
permalink: /teaching/cs4501_fall_24/index
---

Reinforcement learning (RL) is a powerful framework for solving sequential decision making problems
and has enjoyed tremendous success, e.g., [playing the game of Go](https://www.nature.com/articles/nature16961) and [training ChatGPT](https://chat.openai.com/auth/login).
This course is designed to cover basic but important ideas of RL, as well as milestone papers in deep RL if time permits.

## Logistics

- Instructor: [Shangtong Zhang](/)
- TAs:
  - [Ethan Blaser](ehb2bf@virginia.edu) (head TA)
  - [Jiuqi Wang](xgu3km@virginia.edu)
  - [Shuze Liu](shuzeliu@virginia.edu)
- Location: Thornton Hall E303
- Time: Tuesday & Thursday, 11:00 - 12:15  
- Office Hours: 
  - TBA 
- [UVACanvas](https://canvas.its.virginia.edu/courses/115999)
- Prerequisite:
  This course will be light in math but still requires basic ideas of probability, linear algebra, and calculus. The homework is programming-based so you need to be proficient in Python.
- If you need approval for registration,
please move forward directly by submitting the proper forms,
assuming I will approve it.
All the information I have about this course is available on this website,
so please exercise your judgment.
Different schools and colleges have different required forms.
It is your responsibility to figure out which form to submit and where to submit it - this is another hidden prerequisite for this course.
I will not be able to manually handle any individual enrollment / permission  request until near the end of the enrollment deadline.

## Teaching
- Textbook: We will use [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) (RLAI) as the textbook.
You can download a free version of RLAI from the previous link.
- Lectures: **All lectures are whiteboards. To encourage attendance, there will be no slides or notes. But I am sure you can find everything in RLAI.**
As a courtesy,
I will try my best to record each lecture (though not guaranteed) and post the recordings in Canvas.
That being said, it might be good to factor this whiteboard format into consideration when enrolling in this course.

## Grading

The homework of this course is to reproduce representative empirical results in the RLAI book. 
You must use Python.
There are 20 tasks (figures / examples) in total.
Each task has 5 points.
The due date for each task is to be determined according to the course progress.
If we are not able to cover some necessary background of a task, the points of that task will be given for free.
Similarly, if we are able to cover all,
we will additionally discuss deep RL and have some corresponding bonus tasks.
There is no exam or project, no written homework.
The programming tasks are the only way to earn points.

The workload seems heavy but is definitely doable. When I took my first RL course, I reproduced ALL the figures, not just the selected ones below.
I will curve (towards higher points) to give letter grades if necessary.


Homework 1 (Bandit)
* 1.1 Reproduce Figure 2.3 (optimistic initialization)
* 1.2 Reproduce Figure 2.4 (UCB)
* 1.3 Reproduce Figure 2.5 (gradient)
* 1.4 Reproduce Figure 2.6 (parameter study)

Homework 2 (Dynamic Programming)
* 2.1 Reproduce Figure 3.2 (policy evaluation)
* 2.2 Reproduce Figure 4.1 (policy iteration)
* 2.3 Reproduce Figure 3.5 (value iteration)

Homework 3 (Monte Carlo)
* 3.1 Reproduce Figure 5.1 (on-policy)
* 3.2 Reproduce Figure 5.3 (off-policy)
* 3.3 Reproduce Figure 5.4 (off-policy)

Homework 4 (Temporal Difference)
* 4.1 Reproduce Example 6.2 (TD)
* 4.2 Reproduce Figure 6.2 (TD v.s. Monte Carlo)
* 4.3 Reproduce Example 6.5 (SARSA)
* 4.4 Reproduce Example 6.6 (SARSA v.s. Q-learning)
* 4.5 Reproduce Figure 6.5 (double Q-learning)

Homework 5 (N-Step TD)
* Reproduce Figure 7.2

Homework 6 (Approximate Methods)
* 6.1 Reproduce Figure 9.1 (state aggregation)
* 6.2 Reproduce Figure 9.2 (linear function approximation)

Homework 7 (Policy Gradient)
* 7.1 Reproduce Example 13.1 (stochastic policy)
* 7.2 Reproduce Figure 13.1 (REINFORCE)

<!-- ## Roadmap (TBA): -->

<!-- | Date  |  Comments |
|-------| ----------|
|01/18||
|01/23||
|01/25||
|01/30||
|02/01||
|02/06||
|02/08||
|02/11| HW 1 Due. Project proposal Due. |
|02/15||
|02/20| No lecture (tentative). |
|02/22||
|02/25| HW 2 Due.|
|02/27||
|02/29||
|03/05| No lecture. Spring recess.|
|03/07| No lecture. Spring recess.|
|03/10| HW 3 Due.|
|03/12||
|03/14||
|03/19||
|03/21||
|03/24| HW 4 Due.|
|03/26||
|03/28||
|04/02||
|04/04||
|04/07| HW 5 Due.|
|04/09||
|04/11||
|04/16||
|04/21| HW 6 Due.|
|04/18||
|04/23||
|04/25||
|04/30| Last lecture.|
|05/05| Project presentation and writeup due.| -->

## Policies:

- Late Policy:
Late submission within 8 hours (a grace period) has no penalty.
Late submission within 24 hours loses 33% of the scores.
Late submission within 48 hours loses 66% of the scores.
Late submission after 48 hours loses all scores.
No late submission is allowed for the final projection presentation and writeup.
No exception will be made unless doctor notes or [SDAC](https://www.studenthealth.virginia.edu/SDAC) notifications are provided.
- Regrading Policy: For every task, one regrading request is allowed. 