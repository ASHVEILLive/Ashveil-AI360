# 🌐 Ashveil: Real-Time Interactive AI Worlds via 360° Video & Chat Input

## 🧬 What is Ashveil?

Ashveil is an experimental framework turning **360° livestreams** into **interactive AI-driven environments**, where **Twitch viewers and chat commands** actively shape the visuals, mood, and event flow in real time. Think: *Black Mirror meets IRL streaming meets AI hallucination engine*.

This is not a game. This is a **genre-defining platform for storytelling, immersion, and collaboration**, where the stream becomes a malleable, reactive world, not just a window.

---

## 🔥 Why This Matters

- Twitch is passive. Ashveil makes it active.
- 360° streams are underused. Ashveil transforms them.
- Generative AI is everywhere. But Ashveil gives it **purpose and play**.

This isn't another LLM chatbot. This is the real-time merging of **player imagination**, **AI generation**, and **live video** into something truly new.

---

## 🧠 What We’re Looking For (Core Team Roles)

| Role                         | Description |
|------------------------------|-------------|
| 🎮 **Unity/Unreal Dev**       | Build visual overlays and game logic controllers |
| 🧠 **AI/ML Engineer**         | Create SD/ComfyUI pipelines to overlay live video |
| 🌐 **Backend Developer**      | Handle Twitch IRC/webhooks → AI transformation triggers |
| 📹 **360° Stream Specialist** | Help us test with live video (or simulate it) |
| 🛠 **Prompt Engineer / LLM Dev** | Build command-to-event translators (GPT, Claude, etc.) |
| 🧪 **Prototype Hacker**       | Help us make the MVP fast — no egos, just fire |

> If you can build fast, love generative media, and think “impossible” means “Tuesday” — you’ll fit right in.

---

## 🛠️ Tech Stack (Flexible but Focused)

| Layer         | Stack Candidates |
|---------------|------------------|
| **Stream Input**  | Insta360, OBS RTMP, YouTube 360 APIs |
| **Processing**    | Python, ComfyUI, SDXL, FFmpeg, WebRTC |
| **AI Gen Layer**  | Stable Diffusion, ControlNet, AnimateDiff |
| **Twitch API**    | Twitch IRC, WebSockets, PubSub |
| **Scene Engine**  | Unity (URP) or Unreal (Niagara) |
| **Language Layer**| GPT-4/Claude for command translation |
| **Backend API**   | FastAPI, Supabase, or Node/Express |
| **Orchestration** | Webhooks + internal command pipeline |

---

## 🧭 Phase One Roadmap: MVP Build

### ✅ PART 1: Skeleton + Sim Stream

- [ ] Set up repo & structure
- [ ] Simulated 360° stream (recording okay)
- [ ] Twitch Chat listener (parse for !commands)
- [ ] AI prompt templates (scene modifiers)
- [ ] ComfyUI pipeline accepts input > generates frame
- [ ] Re-output as Twitch-compatible stream

### 🧪 PART 2: World Feedback Loop

- [ ] Basic environmental logic (rain, sun, shift)
- [ ] Hook chat intensity (voting system) to event triggers
- [ ] Audio-reactive or emotion-reactive features
- [ ] Scene memory (e.g., “the storm comes back if ignored”)

---

## 🗂 Suggested Folder Structure

ashveil/ ├── api/ │ └── websocket_listener.py ├── ai/ │ ├── prompts/ │ ├── comfy_pipeline.json ├── stream/ │ ├── video_input_handler.py │ └── output_overlay_composer.py ├── engine/ │ └── unity_logic_controller.cs ├── commands/ │ └── twitch_parser.py ├── frontend/ │ └── obs_layouts/ ├── README.md ├── LICENSE └── IP_NOTICE.md

---

## 🔐 IP Protection Notice (MIT + Attribution Clause)

All contributions fall under an extended **MIT license** with attribution and IP retention by Ashley Gray.

If you're contributing:
- You retain your code credit.
- The **concept and system** remain under Ashley Gray’s creative direction.
- Commercial use will be negotiated before release.

> This protects all collaborators **and** the integrity of the vision. If we win, we win together.

---

## 📬 How to Get Involved

1. Open a PR or Issue with your proposed component or skillset
2. DM me or email with your GitHub & previous AI work (if any)
3. Drop into `#ashveil-dev` Discord (link TBA)
4. Show up. Build fast. Dream big.

---

## 🧠 Vision

> "Ashveil is an IRL hallucination engine. The audience is the world builder. AI is the paintbrush. And we’re just getting started."

—

**Made with obsession and intention by Ashley Gray.**  
*April 11, 2025 – IP logged and timestamped.*

