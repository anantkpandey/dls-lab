
import json
import statistics
import time
import urllib.error
import urllib.request

URL = "http://127.0.0.1:8080/"
REQUESTS = 1000
WARMUP_REQUESTS = 20
TIMEOUT_SECONDS = 5


def request_once():
    start = time.perf_counter_ns()

    with urllib.request.urlopen(URL, timeout=TIMEOUT_SECONDS) as response:
        status = response.status
        body = response.read()

    elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000

    if status != 200:
        raise RuntimeError(f"Unexpected HTTP status: {status}")

    json.loads(body)
    return elapsed_ms


def percentile(values, p):
    ordered = sorted(values)
    index = round((p / 100) * (len(ordered) - 1))
    return ordered[index]


def main():
    print(f"Target: {URL}")
    print(f"Warm-up requests: {WARMUP_REQUESTS}")
    print(f"Measured requests: {REQUESTS}")

    for _ in range(WARMUP_REQUESTS):
        request_once()

    latencies = []
    failures = 0

    benchmark_start = time.perf_counter()

    for _ in range(REQUESTS):
        try:
            latencies.append(request_once())
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            failures += 1
            print(f"Request failed: {exc}")

    elapsed_seconds = time.perf_counter() - benchmark_start

    if not latencies:
        print("No successful requests. Check whether the server is running.")
        return

    print("\n--- Benchmark Results ---")
    print(f"Successful requests: {len(latencies)}")
    print(f"Failed requests:     {failures}")
    print(f"Elapsed time:        {elapsed_seconds:.3f} seconds")
    print(f"Throughput:          {len(latencies) / elapsed_seconds:.2f} requests/second")
    print(f"Mean latency:        {statistics.mean(latencies):.3f} ms")
    print(f"Median latency:      {statistics.median(latencies):.3f} ms")
    print(f"P95 latency:         {percentile(latencies, 95):.3f} ms")
    print(f"P99 latency:         {percentile(latencies, 99):.3f} ms")
    print(f"Minimum latency:     {min(latencies):.3f} ms")
    print(f"Maximum latency:     {max(latencies):.3f} ms")


if __name__ == "__main__":
    main()
