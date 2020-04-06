"Indian guessing"  was a challenge in the [Midnight Sun CTF 2020 Quals](https://ctftime.org/event/935).

I initially started writing this programme to figure out what to do, now that the CTF is over, I've cleaned up the code and completed the script with the flag, thought I might aswell publish my version if somebody wanted to use this somewhere.



If you want to know how to solve this:
<details>
"The service read a float from stdin and tries to approximate it using bisection. If the approximation is close enough we lose.

Therefore, we could send a NaN since it's a valid float and by specification NaN != NaN" 
Source: [https://ctftime.org/writeup/19344](https://ctftime.org/writeup/19344)
</details>
