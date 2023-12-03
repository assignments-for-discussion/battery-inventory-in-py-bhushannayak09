
def count_batteries_by_health(present_capacities):
    healthy_count = 0
    exchange_count = 0
    failed_count = 0
    rated_capacity = 120

    for present_capacity in present_capacities:
        
        soh = (present_capacity / rated_capacity) * 100

      
        if soh > 80:
            healthy_count += 1
        elif 62 <= soh <= 80:
            exchange_count += 1
        else:
            failed_count += 1

    return healthy_count, exchange_count, failed_count

# Test function
def test_classify_batteries():
    # Test case 1: All batteries are healthy
    assert classify_batteries([120, 115, 118, 110, 112]) == (5, 0, 0)

    # Test case 2: Mix of healthy, exchange, and failed batteries
    assert classify_batteries([105, 90, 75, 78, 82]) == (1, 2, 2)

    # Test case 3: All batteries have failed
    assert classify_batteries([55, 50, 40, 30, 62]) == (0, 0, 5)

    # Test case 4: All batteries need exchange
    assert classify_batteries([70, 65, 68, 62, 63]) == (0, 5, 0)

    # Additional test case: Empty list
    assert classify_batteries([]) == (0, 0, 0)

    print("All tests pass!")

# Run the tests
test_classify_batteries()


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
