Step 1: Send a normal request to the live service
The service is deployed and accessible at the public URL. To observe its normal behavior, send a single POST request to the /vulnerable endpoint.
On macOS or Linux, open a terminal and run:

curl -X POST https://cloudfunctionexpolitdetector.onrender.com/vulnerable \
  -H "Content-Type: application/json" \
  -d '{"hello":"world"}'

On Windows, open PowerShell and run:

Invoke-RestMethod -Uri "https://cloudfunctionexpolitdetector.onrender.com/vulnerable" `
  -Method POST `
  -Body '{"hello":"world"}' `
  -ContentType "application/json"

The service responds with:
{"status":"processed"}

This shows how the application behaves under normal usage.


Step 2: Generate high-frequency requests (spam simulation)
Next, simulate abusive or high-frequency traffic by sending many POST requests in a short time. This represents how a publicly exposed cloud-style endpoint can be misused.

On macOS or Linux, run the following command once:
```bash
for i in {1..300}; do
  curl -s -X POST https://cloudfunctionexpolitdetector.onrender.com/vulnerable \
    -H "Content-Type: application/json" \
    -d '{"spam":"yes"}' > /dev/null
done
```

On Windows, run this command once in PowerShell:
```powershell
1..300 | ForEach-Object {
  Invoke-RestMethod -Uri "https://cloudfunctionexpolitdetector.onrender.com/vulnerable" `
    -Method POST `
    -Body '{"spam":"yes"}' `
    -ContentType "application/json" | Out-Null
}
```

No output appears in the terminal or PowerShell window. This is expected because the responses are intentionally suppressed.


Step 3: Observe runtime behavior
While the high-frequency requests are being sent, the application continues to run normally without interruption. From the client side, there is no visible difference other than the absence of printed responses.


Step 4: Review server-side logs

After running the spam command, open the Render dashboard and view the logs for the deployed service. In the logs, a burst of entries appears within a short time window, all coming from the same IP address and repeatedly accessing the /vulnerable endpoint. This log pattern represents abnormal traffic.


Step 5: Result interpretation

The normal request demonstrates standard operation, while the burst of requests demonstrates how excessive traffic can be generated against an exposed endpoint. The corresponding spike in logs provides clear evidence of abnormal behavior, completing the exploit simulation and observation workflow.
