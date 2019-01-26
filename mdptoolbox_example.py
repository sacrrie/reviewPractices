import mdptoolbox.example

P,R=mdptoolbox.example.forest()
vi = mdptoolbox.mdp.ValueIteration(P,R,0.9)
vi.run()

print vi.policy
