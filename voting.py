from collections import Counter
c =['john','tom','tom','tom','tom','tom',
	'jamie','tom','tom','chris','tony','tony','tony']
vote_count=Counter(c)
max_votes=max(vote_count.values())
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
print("The Winning Candidate is:")
print(sorted(lst)[0])
