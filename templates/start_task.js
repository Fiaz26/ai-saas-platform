async function runAI(prompt) {

    const res = await fetch("/api/v1/tasks/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + localStorage.getItem("token")
        },
        body: JSON.stringify({
            prompt,
            api: "ai-writer"
        })
    });

    const data = await res.json();

    return data.task_id;
}
async function checkStatus(taskId) {

    const res = await fetch(`/api/v1/tasks/status/${taskId}`, {
        headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
        }
    });

    return await res.json();
}
