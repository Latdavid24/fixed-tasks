
#!/bin/bash
# pytest is baked into the environment image (environment/Dockerfile).
mkdir -p /logs/verifier

pytest /tests/test_outputs.py --ctrf=ctrf.json > /logs/verifier/test_output.txt

# Write reward based on test outcome
if [ $? -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi