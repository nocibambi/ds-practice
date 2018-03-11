# Stating a problem

In probability theory it is more important how we state a problem, than in other, more straightforward areas.

## The Birthday problem
> How many people do we need to have in a room before there’s at least a 50% chance that two share a birthday?

This is not specific enough

## Independence
We assume that birthdays are independent. The knowledge of one birthday gives no information about the another.

A more specific form of the question:
> Assume each day of the year is as likely to be someone’s birthday as any other day. How many people do we need to have in a room before there’s at least a 50% chance that two share a birthday?

## Distribution
However, it is still to vague because we assume that we have a random group of people. To simplify, we assume uniform an  distribution of birthdays.
> Assuming that the birthdays of our guests are independent and equally likely to fall on any day of the year (except February 29), how many people do we need to have in the room before there’s at least a 50% chance that two share a birthday?

# Solving the problem

## Dirichlet’s famous Pigeon-Hole Principle
In Appendinx A.11.
Worst case scenario is 365, the minimum working solution is 2.

## Deduction from conditions
There should be at least 50% chance when there is 184 people.

## Brute force calculation
The number of successes divided by the number of possibilities
 * For two persons: $ P =  365 / 365 ^ 2 \approx .27 $
 * For three persons: $ P =  3 * (365 * 1 * 364) / 365 ^ 3 \approx .82$

Lessons:
* **Avoid double counting**
* **Be exhaustive about all the possible cases**

# The complementary event
Sometimes it is hard to calculate the original, so one can calculate rather the complementary event.

An event and its complementary are
 * Independent
 * Mutually exclusive

Independent events' probabilities are multiplicative: The probability that the two independent events occur is $p * q$.

The probability of no shared birthday among n people is $ \prod_{ k= 0}^{n -1 } \frac {365 - (n-1)} {365} = \frac {365!}{365^n * (365 - n)! } $

```Mathematica
(* Mathematica code to compute birthday probabilities *)
(* initialize list of probabilities of sharing and not *)
(* as using recursion need to store previous value *)
noshare = {{1, 1}}; (* at start 100% chance don’t share a bday *)
share = {{1, 0}}; (* at start 0% chance share a bday *)
currentnoshare = 1; (* current probability don’t share *)
For[n = 2, n <= 50, n++, (* will calculate first 50 *)
{
newfactor = (365 - (n-1))/365; (*next term in product*)
(* update probability don’t share *)
currentnoshare = currentnoshare * newfactor;
noshare = AppendTo[noshare, {n, 1.0 currentnoshare}];
(* update probability share *)
share = AppendTo[share, {n, 1.0 - currentnoshare}];
}];
(* print probability share *)
Print[ListPlot[share, AxesLabel -> {"n", "Probability"}]]
```

```python
# Mathematica code to compute birthday probabilities.
# Initialize list of probabilities of sharing and not as using recursion need to store previous value.
noshare = {{1, 1}} # At start, 100% chance don’t share a birthday.
share = {{1, 0}} # At start, 0% chance share a birthday.
currentnoshare = 1 # Current probability don’t share.

For[n = 2, n <= 50, n++, # Will calculate first 50.
{
newfactor = (365 - (n-1))/365 # Next term in product.
# Update probability don’t share.
currentnoshare = currentnoshare * newfactor
noshare = AppendTo[noshare, {n, 1.0 currentnoshare}]
# Update probability share.
share = AppendTo[share, {n, 1.0 - currentnoshare}]
}]
# Print probability share.
Print[ListPlot[share, AxesLabel -> {"n", "Probability"}]]
```
