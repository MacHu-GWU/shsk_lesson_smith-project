---
description: "Thirty scenario questions to run yourself through after the course: how Vercel and GitHub fit together, the environment and branch rules, the standard release workflow, and what to do when something breaks."
---

# Vercel Basics: Prove You Get It

> Thirty questions to run yourself through once the course is behind you. They're scenarios rather than definitions, because knowing what happens is the easy half and knowing why is the half that holds up under pressure. Answer each one yourself before reading the reference. The deep dive underneath is where the reasoning lives, and every question ends with a pointer back to the section it came from.

## 1. What Vercel Actually Solves

**Question**

> Ten years ago, putting a website online meant owning all of this yourself: a server that stays up around the clock, a firewall with the right ports open, a domain with DNS pointed at it, an HTTPS certificate you requested and then remembered to renew three months later, some way to bring a crashed process back, a stack for collecting and searching logs, extra machines and a load balancer once traffic grew, a CDN once overseas visitors started complaining, and an upload-restart-verify ritual you performed by hand after every code change.
>
> Take four or five of those and explain what Vercel does that makes each one stop being your problem.

**What This Tests**

> The list is printed right there, so reciting it back proves nothing. What counts is whether you can attach each item to something Vercel concretely does, which is a decent proxy for understanding what the platform handles on your behalf.

**Reference Answer**

> **Servers and automatic restarts**: the concept of a machine never comes up. You hand over code and it runs. If it crashes, that gets dealt with and you don't hear about it.
>
> **Domains and HTTPS**: a finished deployment arrives with a working URL. Certificates get issued and renewed for you, and you never touch one.
>
> **Logs**: on by default, nothing to configure. Build-time output goes to the Build Log, run-time output to the Runtime Log, and both are searchable.
>
> **CDN and scaling**: global distribution is the resting state. You pick no regions and add no machines when traffic climbs.
>
> **The manual release ritual**: the GitHub integration replaces it. Commit to the repo, Vercel notices, rebuilds, redeploys. There's no button.

**Deep Dive**

> Worth carrying out of this one: **complexity doesn't disappear, it relocates.** Firewalls didn't stop mattering. Somebody configured one, and that somebody was Vercel.
>
> Keeping that straight protects you from a genuinely dangerous illusion, the sense that all the low-level machinery is gone. It's still running. It just isn't yours today, and the day your requirements outgrow the platform's defaults it lands back on your desk.
>
> Where it comes from: [section 5 of 01-why-vercel, "Ten Years Ago, How Many Hurdles Stood Between You and a Live Website"](../01-why-vercel/README.md), and [section 5 of 02-sign-up-vercel, "What Vercel Is Actually Doing for You"](../02-sign-up-vercel/README.md).

---

## 2. Explaining Vercel to Someone Non Technical

**Question**

> A friend with no technical background asks what Vercel is. Give them one sentence, then unpack the specific things it does.

**What This Tests**

> Where you draw the platform's boundary. Too narrow and you leave out most of the value. Too wide and your friend walks away thinking it writes the code for you.

**Reference Answer**

> One sentence: Vercel is a platform that turns your code into a website.
>
> Four things, concretely. It builds your code into a working site. It gives that site a public URL. It makes that URL fast to reach from anywhere in the world. And it records what happens while the site runs, so there's something to read when things go wrong.

**Deep Dive**

> Writing your code isn't on the list. Vercel picks up **at the point where working code already exists**.
>
> That boundary isn't trivia. It tells you which half of the system to search when something breaks. A number rendering wrong on the page is a code problem. A site that won't load at all is a deployment problem. Confuse the two and you'll spend an afternoon in the wrong half.
>
> Where it comes from: [section 5 of 02-sign-up-vercel, "What Vercel Is Actually Doing for You"](../02-sign-up-vercel/README.md).

---

## 3. Finding Out How Close You Are to the Ceiling

**Question**

> You're running a few projects on Hobby and want to know where you stand. Where do you look? And if you blow past a limit one day, what happens? Does a bill show up?

**What This Tests**

> Two things at once: whether you know usage is checkable live, and whether your read on the consequences is accurate. The second one decides how boldly you're willing to use the platform at all.

**Reference Answer**

> Usage is live on the usage page in the Vercel Dashboard. Docs give you static figures; the usage page gives you your actual position, and both are worth being able to read.
>
> Going over doesn't generate a bill. Hobby is free with no billing cycle attached, so crossing a limit gets that capability paused and restored after thirty days rather than metered. Worst case something stops working. You don't owe anybody money.
>
> Rough limits: a million requests a month, a million function invocations, two hundred projects, a hundred deployments a day. Those numbers move, so check the pricing page and the Hobby docs when you need current ones.

**Deep Dive**

> Nobody's asking you to memorize numbers. Two structural facts are what matter.
>
> First, **project count and daily deployment count are capped too**. Free plans get assumed to be unlimited in exactly those two places, and they aren't: two hundred projects, a hundred deployments a day. Plenty for learning, but knowing a ceiling exists and assuming there isn't one are very different states of mind.
>
> Second, **going over pauses you instead of billing you**. Pay-as-you-go platforms keep serving past your quota and then invoice you, which is where every five-figure horror story comes from. Hobby hard stops, so your exposure is bounded. Carry the question forward to the next service you sign up for: does exceeding a limit pause me or keep charging me? That one question filters out most of the financial risk you'll ever face with cloud tools.
>
> Where it comes from: [section 6 of 02-sign-up-vercel, "Is the Free Plan Enough, and Will You Get Charged"](../02-sign-up-vercel/README.md).

---

## 4. Your Side Project Starts Making Money

**Question**

> A small tool you put on Hobby turns out to have people willing to pay for it, and you decide to take it seriously. One thing needs handling immediately. What is it?

**What This Tests**

> Whether you read the terms before building on a free service. Nothing here ever throws an error, so the only people who act on it are the ones who knew going in.

**Reference Answer**

> Upgrade the plan. Fair use terms limit Hobby to **non-commercial, personal use**. Learning, portfolios, and personal projects are all fine. The moment money is involved you're out of compliance, and it's time to move to Pro.

**Deep Dive**

> What makes this one nasty is the total absence of feedback. Run a commercial project on Hobby and nothing happens, for however long it takes the platform to notice, and then something does. Textbook slow-surfacing mistake.
>
> The only defense against that whole category is knowing it exists before you start, since cleanup always costs more than the five minutes of reading would have.
>
> Where it comes from: the closing part of [section 6 of 02-sign-up-vercel, "Is the Free Plan Enough, and Will You Get Charged"](../02-sign-up-vercel/README.md).

---

## 5. Your Friend Thinks Signing Up Is a Hassle

**Question**

> A friend signing up spots the "Continue with GitHub" button and calls it the fastest way in, no extra password to remember. Do you talk them out of it? How?

**What This Tests**

> A professional habit: keeping accounts independent. The call costs nothing today and a lot later, so arguing it well says you think about risk structurally.

**Reference Answer**

> Yes, talk them out of it, and point them at an independent email address.
>
> The issue is where the credentials end up. Sign in through GitHub and your Vercel credentials now live inside GitHub. If that GitHub account ever has trouble, whether an anti-abuse system flags it as a bot or a forgotten password drops them into a recovery process that stalls, the Vercel account goes down with it and everything deployed underneath is affected.
>
> An independent email keeps the Vercel account tied to their own inbox, where nothing happening at another company can reach it.
>
> Same logic one step further: don't use a work email for personal accounts either. Work email gets switched off when you change jobs, and everything hanging off it goes too.

**Deep Dive**

> Quick test for this: if this third-party account vanished tomorrow, could I still get into the service? Yes means it's a data source. No means it's your front door, and you want to own your own front door.
>
> You'll sign up for hundreds of services over a career. Nest them all inside each other and the day one link snaps, most of your time goes into working out which link it was.
>
> An objection comes up right away here: doesn't deploying require authorizing Vercel to reach GitHub anyway? Different relationship entirely. See question 9.
>
> Where it comes from: [section 7 of 02-sign-up-vercel, "Why Email Instead of Signing In Through GitHub"](../02-sign-up-vercel/README.md).

---

## 6. You Just Clicked Deploy

**Question**

> You pick a Template from the gallery and hit Deploy. In the minute or two you spend waiting, what two things actually happen? Why does their order matter?

**What This Tests**

> Whether you can break a button that looks like magic into concrete actions. Several later questions assume this chain, and without it, everything about environments and debugging has nothing solid to sit on.

**Reference Answer**

> Two things happen, not one.
>
> The first happens on GitHub. Vercel creates a new repository under my account and copies the Template's code into it verbatim. From that point the code is mine, with no remaining tie to the original author's repo.
>
> The second happens on Vercel. That new repository gets registered as a project, and Vercel reads the code, builds it, and deploys it.
>
> Order matters because it fixes the direction of everything downstream: **code lands in GitHub first, then flows from GitHub into Vercel**. Once that's clear, automatic deployment stops being mysterious. Vercel is watching my repo, so every future commit gets noticed, rebuilt, and redeployed without me pressing anything.

**Deep Dive**

> Worth settling what a Template is while we're here. It's a public GitHub repository holding a complete project somebody already wrote and verified. No Vercel-specific magic inside it.
>
> Questions 7 and 8 both lean on this chain. A surprising number of problems that look unrelated turn out to be explainable by walking along it.
>
> Where it comes from: [section 5 of 03-deploy-your-first-app, "What a Template Actually Is"](../03-deploy-your-first-app/README.md).

---

## 7. You Want to Fix One Sentence on the Site

**Question**

> There's a typo in some copy on your site. Where do you go to fix it, and why isn't the answer somewhere in the Vercel interface?

**What This Tests**

> Whether the direction of the chain is straight in your head. People who have it backwards hunt around Vercel for an edit button, then decide their permissions must be wrong.

**Reference Answer**

> You change the code in the GitHub repo.
>
> **The GitHub repo is the single source of truth.** What the website shows is determined entirely by what the code in that repo says. Vercel watches the repo and rebuilds when a new commit appears, which makes it the executor rather than the place content lives.
>
> So edit on GitHub and commit. Vercel takes it from there.

**Deep Dive**

> This sense of direction triages a whole class of problems, because it cuts the system in two. GitHub owns what the content is. Vercel owns turning that content into a website. Decide which half a problem belongs to and you've halved the search space before looking at anything.
>
> Content wrong? Read the code on GitHub instead of digging through Vercel settings. Code on GitHub clearly right? The problem is on the Vercel side, so open the build log.
>
> Where it comes from: the second half of [section 5 of 03-deploy-your-first-app, "What a Template Actually Is"](../03-deploy-your-first-app/README.md).

---

## 8. You Pushed Code and Vercel Did Nothing

**Question**

> You edited and committed on GitHub. Several minutes later the Deployments page still shows nothing new. Where do you start?

**What This Tests**

> Whether you can use the chain from question 6 to localize a fault. People who know the chain go to one link. People who don't wander through settings pages.

**Reference Answer**

> Walk the chain. Normally I commit to GitHub, GitHub notifies Vercel, Vercel starts building. No new deployment record means it stalled at **the notification step**, which is the connection between GitHub and Vercel.
>
> So that's where I look. Is the Vercel project still connected to this repo, is the authorization still in place on the GitHub side, did anybody revoke it.
>
> One dumb possibility to clear first: confirm I committed to the repo this project is connected to and not somewhere else entirely.

**Deep Dive**

> The technique is the real content. **Draw the healthy chain first, then hunt for the broken link.** That beats wandering through settings, and it transfers to any system you'll ever touch.
>
> Notice you never needed to know which specific setting to click. Getting to "the problem is at the connection step" is already enough to search usefully or to ask an AI something worth answering. The course keeps circling this point: localizing beats fixing.
>
> Where it comes from: [section 5 of 03-deploy-your-first-app, "What a Template Actually Is"](../03-deploy-your-first-app/README.md), and [section 8 of 04-deployment-environment-and-git-branch, "The Branch Decides Which Label Gets Applied"](../04-deployment-environment-and-git-branch/README.md).

---

## 9. The Authorization Screen Pops Up

**Question**

> Partway through your first deployment, a GitHub page asks whether you want to let Vercel access your GitHub account. Does that contradict the advice in question 5 about not signing in with GitHub?

**What This Tests**

> The easiest question here to talk yourself out of. It checks whether authentication and authorization stay separate in your head instead of collapsing into "connecting two accounts."

**Reference Answer**

> No contradiction. These are two different relationships.
>
> | Dimension | Signing in to Vercel with GitHub | Authorizing Vercel to access GitHub |
> | :--- | :--- | :--- |
> | What GitHub is | My **front door** into Vercel | A **data source** |
> | Where my credentials live | Parked over on GitHub | Still my own email and password |
> | If this link breaks | I can't get into Vercel at all | I lose a data pipe, account is fine |
> | Can I revoke it | Revoking locks me out | Yes, revoke in settings and move on |
>
> A front door is a lock mounted on somebody else's wall, so when the wall comes down I'm outside. A data pipe is something I ran in myself, and I can pull it whenever I like.
>
> The authorization is genuinely required, since Vercel has to create a repo and read code in my GitHub account, and these are two unrelated companies. Somebody has to say yes once. Once is enough.

**Deep Dive**

> One line worth keeping: separate your front door from your data sources.
>
> The mechanism is OAuth, and it exists so a third party can get limited, revocable access without ever seeing your password. Once that's clear, third-party sign-in stops looking like the same risk. Authorization is revocable and leaves your account intact. Sign-in leaves you locked out the moment it breaks.
>
> Where it comes from: [section 6 of 03-deploy-your-first-app, "What the GitHub Authorization Step Is Doing"](../03-deploy-your-first-app/README.md).

---

## 10. Which Changes Need the Backend

**Question**

> Sort these into changes that touch only static content and changes that make a backend function run: (a) changing the copyright year in the footer from 2025 to 2026; (b) a user clicks a button and the page shows a sentence returned by the server; (c) swapping out the site logo; (d) a user types a keyword into a search box and the page lists matching results.
>
> Have the static versus dynamic distinction in mind before you start.

**What This Tests**

> Whether the distinction survives contact with concrete cases. It pays off directly in debugging, since it decides which side of the system is holding the evidence.

**Reference Answer**

> | Change | Type | Why |
> | :--- | :--- | :--- |
> | (a) Copyright year becomes 2026 | Static | Identical for everyone at any time, hard-coded into the source |
> | (b) A click shows a sentence from the server | Dynamic | That sentence has to be requested |
> | (c) Swap the logo image | Static | One fixed image, same for every visitor |
> | (d) A keyword returns matching results | Dynamic | The keyword goes to the backend, which queries and returns |
>
> Dynamic content is a function underneath. Input goes in, output comes back.

**Deep Dive**

> Question 25 uses this directly. The Runtime Log mostly records **what happens when a backend function runs**, so a purely static page request usually leaves no complete trace there.
>
> Which means "the logo didn't show up" will never turn up in the Runtime Log no matter how long you dig. That one belongs to browser developer tools. Flip it around and "I clicked the button and nothing happened" is exactly what the Runtime Log is for.
>
> Not being able to tell them apart means searching somewhere that could never have held the answer, and then starting to suspect a misconfiguration.
>
> Where it comes from: [section 7 of 03-deploy-your-first-app, "A Website Is Static Content Plus Dynamic Content"](../03-deploy-your-first-app/README.md).

---

## 11. Every Row in the Deployment List Has Its Own URL

**Question**

> Open the Deployments page and every record has its own URL, serving its own content, unbothered by the others. Why build it that way?
>
> You'll want the Deployment concept in mind first, especially the immutable part.

**What This Tests**

> Whether you understand immutability and what it buys you. Later questions about rollbacks, comparisons, and debugging all sit on top of it.

**Reference Answer**

> Because a Deployment is a **complete instance** of the website. Not just code, but the built frontend files, the backend functions, the runtime configuration, and the dependencies, packaged and frozen at one moment. A save file in a game is the right picture.
>
> Those instances are **immutable**. Once one exists it stays exactly as it is. There's no editing a Deployment, only creating a new one, and that makes isolation automatic. Each gets its own URL, and one breaking can't touch another.
>
> The payoff: any historical version stays openable, verifiable, and returnable at any time.

**Deep Dive**

> Immutability leads straight to two practical consequences.
>
> Each Deployment carries its own build log, which is why debugging a deployment problem always starts by pinning down which deployment failed. That's question 24.
>
> Old versions never move, which is exactly why rollback exists and why it's fast. That's question 21.
>
> Where it comes from: [section 5 of 04-deployment-environment-and-git-branch, "What Is a Deployment"](../04-deployment-environment-and-git-branch/README.md).

---

## 12. A Pile of Deployments Is Live, So Which One Do Visitors See

**Question**

> Your project has five or six Deployments sitting there, each with different content. A visitor opens your real URL. What decides which one they get?
>
> Have the concept of an Environment in mind before you answer.

**What This Tests**

> Whether you think of an Environment as a pointer or as a container. The container reading is common, and it quietly invalidates every rule that follows.

**Reference Answer**

> One of those Deployments is wearing the Production label. An Environment is a **pointer**, a label stuck to a Deployment, and whichever instance it points at is what visitors get.
>
> It isn't a container. Nothing is stored inside it. It only points.

**Deep Dive**

> The pointer model explains several behaviors at once.
>
> Instant releases: a pointer moves, nothing gets rebuilt, nothing gets copied anywhere.
>
> Instant rollbacks: the old instance never left, so the pointer goes back.
>
> Treat an Environment as a container and none of that computes. You'd picture a release as hauling new code into a production box, and then the speed of it would make no sense.
>
> Where it comes from: [section 6 of 04-deployment-environment-and-git-branch, "What Is an Environment"](../04-deployment-environment-and-git-branch/README.md).

---

## 13. You and a Coworker Each Open a Branch

**Question**

> You're working on `feature-a` and a coworker is working on `feature-b`, and you both commit. How many Previews exist now? How many Productions? Do the two sets of changes interfere?

**What This Tests**

> Whether you noticed that Production and Preview aren't structurally symmetric. Most people describe them as "one is live, one is for testing," and being unable to name the asymmetry means the understanding is still surface level.

**Reference Answer**

> Two Previews, independent, non-interfering, each with its own URL. Exactly one Production, still the same one as before, since nobody committed to the production branch.
>
> They behave differently because they're different kinds of thing:
>
> | Dimension | Production | Preview |
> | :--- | :--- | :--- |
> | What it is | A **label** | A **category** |
> | How many can exist | Exactly one per project | As many at once as you like |
> | How it changes | Peel it off the old Deployment and stick it on a new one, which is what a release is | Anything that isn't Production lands here automatically |

**Deep Dive**

> The asymmetry follows from what each one answers. Production answers what users are seeing right now, and at any moment that question has exactly one answer, so it has to be unique. Preview answers which versions are being validated, and that question naturally has many answers.
>
> One thing worth adding: a single Deployment can wear several labels. Finish testing in Preview, decide to ship, and the Production label lands on that same Deployment, which is now both. Identical content, obviously, since it's literally the same instance.
>
> Where it comes from: [section 6 of 04-deployment-environment-and-git-branch, "What Is an Environment"](../04-deployment-environment-and-git-branch/README.md).

---

## 14. Getting a Coworker to Reproduce a Bug

**Question**

> You found a bug on your branch and sent the Preview URL to a coworker. They report everything works fine. You did push again in the meantime. What went wrong, and which URL should you have sent?

**What This Tests**

> Whether you know Preview has two kinds of URL and how they differ. Small practical detail, and not knowing it produces this exact mixup on teams over and over.

**Reference Answer**

> I sent the **branch URL**, which always points at the latest deployment on that branch. Since I pushed again in between, my coworker opened the newer version, where the bug no longer reproduces.
>
> The **commit URL** is what I should have sent. It's nailed to one specific deployment and never moves, so they'd have seen the exact version I was looking at.

**Deep Dive**

> The gap between those two URLs is the gap between a pointer and a snapshot, which is question 12 wearing a different hat. The branch URL moves. The commit URL doesn't.
>
> Choosing gets easy once you frame it that way. Want somebody to see what this branch looks like right now? Branch URL. What it looked like at a particular moment? Commit URL. Reproducing a bug, comparing before and after, preserving evidence: all commit URL.
>
> Where it comes from: [section 6 of 04-deployment-environment-and-git-branch, "What Is an Environment"](../04-deployment-environment-and-git-branch/README.md).

---

## 15. You Committed to the dev Branch

**Question**

> You finished a change on a branch called `dev` and committed it. Will users see it right away? What's Vercel basing that decision on?

**What This Tests**

> The single most important question in the course to have right. Miss it and you can break production without knowing, at any time.

**Reference Answer**

> Users won't see it. Vercel deploys a Preview automatically and Production stays where it was.
>
> The decision rests on **which branch received the commit**. Default rule: the production branch, `main` unless configured otherwise, means Production. Any other branch means Preview.
>
> So a commit to `main` reaches users immediately, and a commit anywhere else is invisible to them.

**Deep Dive**

> What makes the rule elegant is that it ties an abstract decision, should this go out to users, to a concrete fact you can always see, which branch am I on. The choice never happens through an interface. You look at where you're standing.
>
> It also isolates the only genuinely dangerous moment in the whole workflow, which is committing without checking the branch. Question 20 goes there.
>
> Where it comes from: [section 8 of 04-deployment-environment-and-git-branch, "The Branch Decides Which Label Gets Applied"](../04-deployment-environment-and-git-branch/README.md).

---

## 16. The New Project Calls Its Main Branch master

**Question**

> You join a different project and the team's main branch is `master`, not `main`. Does committing to `master` trigger a Production deployment? How would you confirm?

**What This Tests**

> Whether you memorized the previous rule as dogma. Anyone carrying "main equals live" and nothing else gets this wrong.

**Reference Answer**

> Depends on the configuration, and assuming is the mistake.
>
> Which branch counts as the production branch is **configurable**. `main` is a default value, nothing more, and a team is free to designate `master` or anything else.
>
> Confirm it in project settings, where the production branch is named. The model to carry is "whichever branch is designated production is live," not "main is live."

**Deep Dive**

> The habit is the real subject. When you inherit a project, verify its configuration instead of applying whatever defaults you're used to.
>
> That generalizes well past Vercel. A default is called a default because it can be changed, so any time you learn how something behaves by default, pick up two more facts with it: that it's configurable, and where to go check.
>
> Where it comes from: [section 8 of 04-deployment-environment-and-git-branch, "The Branch Decides Which Label Gets Applied"](../04-deployment-environment-and-git-branch/README.md).

---

## 17. A Brand New Project Goes Straight Live

**Question**

> You create a new Vercel project, and when the deployment finishes it's already Production and publicly reachable, with no Preview offered first. Is that normal? Why?

**What This Tests**

> An easy exception to trip over. Not knowing it leads people to assume they misconfigured something, or worse, to believe they're editing a Preview when they're editing production.

**Reference Answer**

> Normal. **The first deployment of a new project is always Production**, whichever branch it came from.
>
> The Preview rules from question 15 only start applying once a Production deployment exists.

**Deep Dive**

> The reasoning holds up. With no Production deployment yet, making the first one a Preview would protect nothing, because there's no live version to protect.
>
> The consequence is that **the first deployment of a new project has no buffer at all**. Anything in that code that shouldn't be public is public immediately, so look at what's in there before you click.
>
> Where it comes from: [section 8 of 04-deployment-environment-and-git-branch, "The Branch Decides Which Label Gets Applied"](../04-deployment-environment-and-git-branch/README.md).

---

## 18. A Coworker Says to Push It to the dev Environment

**Question**

> A coworker asks you to "push that change to the dev environment and take a look." In Vercel terms, what might they mean? What do you need to clarify?

**What This Tests**

> A common misconception, that Vercel provides a hosted environment called development. It sends people hunting for an entry point that doesn't exist and makes conversations talk past each other.

**Reference Answer**

> Ask, because in a Vercel context that sentence is ambiguous.
>
> The three default environments are Local, Preview, and Production, and they aren't peers. **Local is your own computer**, used for development and debugging, never uploaded to Vercel. Only Preview and Production actually run there.
>
> So the coworker could mean any of three things: run it locally and look; push a branch and look at the Preview; or, if the team is on Pro or above, deploy to a Custom Environment they've named dev. Three different actions, so ask which.

**Deep Dive**

> Custom Environments are a Pro and Enterprise feature, meant for finer distinctions like staging and QA. Hobby doesn't have them, which leaves Preview and Production, and that's plenty for one developer.
>
> The wider point is that "environment" is a high-frequency source of ambiguity on teams, since every company and platform defines it a little differently. Confirming costs one sentence and saves a lot of wasted work.
>
> Where it comes from: [section 7 of 04-deployment-environment-and-git-branch, "Which Environments Vercel Gives You by Default"](../04-deployment-environment-and-git-branch/README.md).

---

## 19. Adding a Feature to a Site That Has Real Users

**Question**

> Your website has people using it and now needs a new feature. Walk through the complete workflow in order, from starting work to users seeing the new version. Which step is the actual release?

**What This Tests**

> The central synthesis question, threading several earlier concepts into a workflow you could execute. The second half checks whether making a change and releasing it are distinct in your head.

**Reference Answer**

> The workflow:
>
> One, branch off `main` into something new, say `development`.
>
> Two, change the code on that branch and commit.
>
> Three, Vercel detects the commit and deploys a Preview. No action from me.
>
> Four, open the Preview URL and verify the change does what I expected.
>
> Five, satisfied, open a Pull Request on GitHub to merge `development` into `main`.
>
> Six, the merge lands, Vercel sees `main` change, deploys, and updates Production.
>
> Seven, users see the new version.
>
> The release is **the merge in step five**. Everything before it, all the editing and committing and deploying and verifying, is invisible to every user.

**Deep Dive**

> The design insight is that this workflow **concentrates the risk into one clearly marked action**. The first four steps are yours to do anything with. Only the merge is serious. Managing one dangerous step is far easier than managing seven mildly dangerous ones.
>
> Also notice you never clicked anything in the Vercel interface. Steps three and six fire on their own, and what fires them is the GitHub to Vercel chain from questions 6 and 7.
>
> Where it comes from: "The Complete Workflow" under [section 8 of 04-deployment-environment-and-git-branch, "The Branch Decides Which Label Gets Applied"](../04-deployment-environment-and-git-branch/README.md).

---

## 20. The Step in That Workflow Most Likely to Burn You

**Question**

> None of the steps in that workflow are hard. One of them, done carelessly, breaks production outright. Which one, and how exactly do you guard against it?

**What This Tests**

> Whether you've actually done this by hand. On the page every step looks equally uneventful, so people who only read about it can't name the dangerous one.

**Reference Answer**

> **Committing without confirming which branch you're on.**
>
> By the rule in question 15, a commit to the production branch is Production, no exceptions. Think you're on `development` while you're still on `main` and that commit skips the entire verification workflow and lands on every user.
>
> The defense is a habit. Glance at the branch selector before editing a file on GitHub. Then, when you fill in the commit message, confirm once more that you're committing to the current branch rather than to some other option in the dropdown.

**Deep Dive**

> This earns its own question because every other step forgives you. Wrong branch created? Delete it and start over. Bad code written? The Preview shows you. Committing to the wrong branch has no buffer whatsoever. You press the button and users have it.
>
> Generalize the move: examine any workflow for its irreversible points, then put one deliberate check exactly there. Far more effective, and far less exhausting, than trying to be careful at every step.
>
> Where it comes from: [section 9 of 04-deployment-environment-and-git-branch, "Exercises"](../04-deployment-environment-and-git-branch/README.md), where confirming the branch comes up at nearly every step.

---

## 21. The New Version Ships and Something Is Wrong

**Question**

> You merged into `main`, Production updated, and now users are reporting the new version is broken. You want the site back on the last known good version as fast as possible. Can you? Why?
>
> Have the immutability of a Deployment and the pointer nature of an Environment loaded before you answer.

**What This Tests**

> Whether you can combine those two concepts into an actual capability. Anyone picturing a release as overwriting can't explain how a rollback is even possible.

**Reference Answer**

> Yes, and fast.
>
> The old version never went anywhere. A release overwrites nothing; it moves a **pointer**, taking the Production label off one Deployment and putting it on another. The old Deployment is still sitting in the list, intact, just no longer Current.
>
> A rollback moves that pointer back onto the older Deployment you know was fine. Nothing rebuilds and no code gets re-uploaded.

**Deep Dive**

> Read questions 11, 12, and this one together and the causal chain closes. Deployments are immutable, so old versions persist. Environments are only pointers, so switching is instant. Together they make rollback fast and safe.
>
> It also explains why modern deployment platforms converged here. Under the old model of copying new files over the ones on a server, rolling back means shipping the old files all over again, which is slow and easy to botch.
>
> One caveat worth stating out loud: a rollback stops the bleeding and cures nothing. You still have to fix the problem on a branch and ship it through the workflow in question 19.
>
> Where it comes from: [section 6 of 04-deployment-environment-and-git-branch, "What Is an Environment"](../04-deployment-environment-and-git-branch/README.md).

---

## 22. Two Kinds of Failure, Two Places to Look

**Question**

> Which log do you open for each: (a) you committed code but nothing on the website changed; (b) the website loads fine, but clicking submit throws an error.
>
> State the rule you used to decide.

**What This Tests**

> Debugging starts with classification, and a wrong class makes everything after it wasted motion. That's what this checks.

**Reference Answer**

> (a) is the **Build Log**. (b) is the **Runtime Log**.
>
> | Dimension | Build Log | Runtime Log |
> | :--- | :--- | :--- |
> | What it records | The deployment process | What happens while backend functions run |
> | When to open it | The site won't load, or content didn't update | The site loads, but a feature misbehaves |
> | What it hangs off | One specific Deployment | The project, under the Logs entry |
>
> In (a) content didn't change, so the new version never deployed successfully, usually because dependencies wouldn't install, code wouldn't compile, or configuration was missing. In (b) the site loads, so the deployment worked and the failure is happening at run time.
>
> The rule is one question: **does the site load?**

**Deep Dive**

> That rule works because it turns on a single fact anybody can check immediately. No understanding the error, no reading the code. Open a browser and try it.
>
> The "what it hangs off" row isn't arbitrary either. It follows from the isolation in question 11. Each deployment runs its own build and therefore owns its own build log, while running is something the whole project does continuously, so runtime logs can only live at the project level.
>
> Where it comes from: [section 6 of 05-view-logs, "Two Kinds of Log: Build Time and Run Time"](../05-view-logs/README.md), which ends with a side-by-side table.

---

## 23. Users Hit a Problem Last Night and You Hear About It This Morning

**Question**

> A coworker tells you this morning that users reported an error in one of the site's features last night. You open the Runtime Log now. Will you find it? What does that change about how you handle production problems?

**What This Tests**

> A fact with real operational consequences. Not knowing it means digging for logs that expired hours ago, or missing the investigation window without ever noticing there was one.

**Reference Answer**

> You won't find it. On Hobby the Runtime Log is **retained for one hour**, and one day on Pro. Last night is long gone.
>
> What changes: **runtime problems have to be investigated while they're happening**. See something wrong, go read the logs right then. And if you can't catch them yourself, you need some other way to hear about them early, because reconstructing them afterward isn't on the table.
>
> The Build Log is the opposite. **Kept permanently**, so a build log from three months ago is still sitting there. The two are nothing alike.

**Deep Dive**

> One hour isn't the point. The behavior that one hour forces is the point.
>
> It also shows why knowing a tool's limits matters as much as knowing its features. Somebody who knows "Vercel has logs" and somebody who knows "runtime logs last an hour on my plan" respond to the same incident at completely different speeds.
>
> If a project genuinely needs long-term retention, the answers are upgrading the plan or configuring Drains to export logs. Both sit outside this course, but knowing the option exists is worth something.
>
> Where it comes from: [section 7 of 05-view-logs, "How Long Each Log Sticks Around"](../05-view-logs/README.md).

---

## 24. Looking Into a Deployment From Three Months Ago

**Question**

> You want to inspect a deployment from three months ago and see what happened during the build. Can you? How do you find it?

**What This Tests**

> The counterpart to the previous question, checking whether the two retention policies stay distinct in your head. It also checks whether you know where build logs live.

**Reference Answer**

> Yes. The Build Log is kept permanently, and every Deployment keeps its own indefinitely.
>
> To find it: open the project's Deployments page, locate that deployment, click into its detail page, expand Build Logs.
>
> The key move is pinning down **which deployment** first, since build logs hang off a Deployment rather than off the project.

**Deep Dive**

> A model worth keeping: where a log lives matches what it records.
>
> Building is something each deployment does once, on its own, so build logs file under a Deployment and last forever, because the Deployment lasts forever.
>
> Running is something the whole project does continuously, so runtime logs sit at the project level, and the sheer volume means they can only be kept for a window.
>
> Where it comes from: [section 7 of 05-view-logs, "How Long Each Log Sticks Around"](../05-view-logs/README.md), and "Exercise 1: Open a Specific Deployment" in the same document.

---

## 25. The Runtime Log Is Empty

**Question**

> You've been digging through the Runtime Log and can't find a single relevant record. List the possible reasons.

**What This Tests**

> Whether you know this tool's boundaries. People who don't search the same wrong place repeatedly, lose time, and start doubting their own configuration.

**Reference Answer**

> A few possibilities.
>
> One, the time range filter is too narrow, or the event fell outside the retention window, which is only an hour on Hobby.
>
> Two, whatever I triggered **never called the backend**. The Runtime Log mostly records what backend functions produce when they run, so a purely static page request generally leaves no complete trace.
>
> Three, the problem lives entirely in the browser: an image that failed to load, broken styling, a frontend script throwing. The server has no idea any of that happened, and browser developer tools are where it surfaces.

**Deep Dive**

> Reasons two and three both rest on the static versus dynamic split from question 10. Knowing whether an interaction actually reached the backend is what tells you which side holds the evidence.
>
> This is one of debugging's classic time sinks. You search somewhere that could never have contained the answer, then start wondering whether your permissions are wrong or your configuration is broken. Knowing the tool's boundaries skips the whole spiral.
>
> Where it comes from: the Runtime Log part of [section 6 of 05-view-logs, "Two Kinds of Log: Build Time and Run Time"](../05-view-logs/README.md), and the checklist in "Exercise 3: Read the Runtime Log" for when no logs appear.

---

## 26. The Deployment Failed and the Screen Is Full of English

**Question**

> Your deployment failed, and the Build Log just handed you several hundred lines you can't make sense of. What now? Walk through it step by step.

**What This Tests**

> Whether the course's central method converts into concrete actions for you. It also tests whether you give an AI enough context, which is where results differ most in practice.

**Reference Answer**

> First, I don't need to understand it myself. I start **at the bottom of the log and read upward**, because a failed deployment puts the useful error in the last several lines and everything above it is routine step-by-step output.
>
> Second, I copy the section around the error along with the last few dozen lines.
>
> Third, I hand that to an AI with context, and the context needs five things: a specific description of the symptom, my read on which stage it belongs to (this one is deployment stage), the raw log, the project's tech stack, and what I changed recently.
>
> Fourth, I apply whatever fix comes back and redeploy to verify.
>
> One line added to the prompt helps: if the log isn't enough to localize the problem, say what else you need instead of guessing.

**Deep Dive**

> The course's position: **you don't need to read the log, you need to know where the log is**. Analyzing error output happens to be something AI is unusually good at. Stack traces and dependency conflicts are hieroglyphics to a person and a pattern the model has seen a million times.
>
> Which leaves a four-step debugging routine. Classify the stage, extract the log, hand it over with context, apply and verify. Only the first two need you.
>
> The bottleneck in debugging is rarely analysis. It's almost always missing information, so one extra minute assembling context saves ten rounds of follow-up questions.
>
> Where it comes from: [section 10 of 05-view-logs, "Mentor's Note"](../05-view-logs/README.md), and the debugging prompt template in "Exercise 4: Turn a Log Into a Question You Can Use".

---

## 27. The Deployment Says It Succeeded and the Site Looks the Same

**Question**

> The deployment shows Ready and everything looks healthy, but you open the website and the content is unchanged. List the possible causes and the order you'd rule them out in.

**What This Tests**

> An open-ended debugging question with no single answer. It checks whether you can assemble several learned rules into a systematic way of narrowing down.

**Reference Answer**

> In the order I'd check them.
>
> One, **I'm looking at the wrong URL**. The deployment that succeeded may have been a Preview while I'm opening the Production URL. Go to the Deployments page and read the label on that record.
>
> Two, **I committed to a branch that isn't the production branch**. By the branch rule that produces a Preview, so Production naturally didn't move. Same cause as the first one, seen from another angle.
>
> Three, **I changed the wrong thing**. Go to GitHub and confirm the commit landed in the file and branch I believe it did.
>
> Four, **browser cache**. Force refresh, or open an incognito window.

**Deep Dive**

> The ordering is the lesson: **suspect that you're looking in the wrong place before you suspect the system broke**.
>
> The first three causes all resolve to the same thing, confusing Production with Preview. That's the single most common source of beginner confusion, because the two URLs look alike, both load fine, and serve different content.
>
> A habit worth building: when a change didn't take effect, open the Deployments page and read the label on that record before refreshing the site again.
>
> Where it comes from: [section 8 of 04-deployment-environment-and-git-branch, "The Branch Decides Which Label Gets Applied"](../04-deployment-environment-and-git-branch/README.md), and "Exercise 5: Compare Preview and Production" in the same document.

---

## 28. The Button the Tutorial Mentions Is Not on Your Screen

**Question**

> You're following a tutorial and the button it tells you to click is nowhere in the interface. What do you do? Which pieces of information does the AI need from you?

**What This Tests**

> How you react when information goes stale, which is most of what learning independently consists of. It also tests whether you give an AI enough to work with.

**Reference Answer**

> Start by recognizing this as normal. You didn't do anything wrong; the platform shipped a redesign. Stop hunting.
>
> Then screenshot the current interface and send it with three things: **the screenshot** (what I see now), **the tutorial text** (what I was told to see), and **my goal** (what I'm trying to accomplish).
>
> Ask where the feature lives now and what to click, step by step. If it was renamed or removed, ask for that plainly along with the replacement.
>
> Close with one line: if you're not sure, tell me which page of the official docs to check instead of guessing.

**Deep Dive**

> Drop any one of those three inputs and the AI is guessing. The screenshot alone doesn't say what you want. The tutorial text alone doesn't say what your screen looks like.
>
> That closing "don't guess" line is a genuinely useful technique. An uncertain model will sometimes invent a plausible-sounding path, and explicitly inviting it to admit uncertainty cuts that down noticeably.
>
> Set this next to question 26 and they're the same move in two settings. Can't find it in the UI, send a screenshot. Something broke, send the log. Underneath both: **find the evidence and hand it to whoever can process it**.
>
> Where it comes from: [section 9 of 01-why-vercel, "Screenshots Expire, the Logic Behind Them Doesn't"](../01-why-vercel/README.md), where the full prompt sits in the code block.

---

## 29. Handing the Project Off to Somebody Else

**Question**

> You're handing a Vercel project to a coworker. Beyond account access, which places do you walk them through, what is each one for, and what do you tell them about the workflow?

**What This Tests**

> A synthesis question about whether you're carrying a complete map of this system. People who can describe the map genuinely know how to use it. People running a fixed procedure leave pieces out.

**Reference Answer**

> At minimum, these.
>
> | Where | What it is for |
> | :--- | :--- |
> | The GitHub repo | The single source of truth. Every content change happens here. Tell them which branch is the production branch |
> | The Deployments page | Every deployment record, labeled Production or Preview, with status, branch, and commit. Debugging a change that seems to have done nothing starts here, and so do rollbacks |
> | The Build Log inside a given Deployment | Where to look when a deployment fails. Kept permanently |
> | The project-level Logs entry | Where to look when something breaks at run time. Warn them the window is short, so it has to be checked on the spot |
> | The usage page | How much headroom is left against the quota |
>
> On workflow, be explicit. Branch first, verify on the Preview, and nothing counts as a release except a merge into the production branch. Always confirm the branch before committing.

**Deep Dive**

> The real question is whether the course turned into a map for you or stayed a sequence of steps.
>
> That difference decides how far you get. Somebody holding a sequence can only walk the path they were shown and stalls when conditions change. Somebody holding a map knows what each part is for and can reason their way to the right place in a situation nobody covered.
>
> Easy test: pair each place above with the question it answers. Deployments answers which code is live right now. The Build Log answers why the deployment failed. Logs answers what happened at run time. The usage page answers how much is left.
>
> Where it comes from: ["Exercise 2: Get to Know the Project Console" in 03-deploy-your-first-app](../03-deploy-your-first-app/README.md), and [section 11 of 05-view-logs, "Quick Reference"](../05-view-logs/README.md).

---

## 30. You Have Seen This Mechanism Before

**Question**

> Vercel's Preview and Production setup, and Git's branches and trunk. How do you think the two relate? Start from how you handle Git branches day to day.

**What This Tests**

> The most open-ended question here, checking whether you recognize the same pattern showing up at different layers. People who can pick up new tools noticeably faster.

**Reference Answer**

> They solve the same class of problem at two different layers.
>
> A Git branch lets you try an idea safely without touching the main line of code. An Environment lets you test a deployment safely without touching users.
>
> Git manages **versions of the code**. An Environment manages **versions of the whole running system**.
>
> The logic underneath is identical. Make an isolated space, experiment freely inside it, merge into the main line only when you're satisfied.

**Deep Dive**

> Recognizing the pattern turns Environments from a fresh set of rules into a familiar idea relocated one layer up. It's also why these two concepts, once they land, never leave.
>
> The pattern runs well past engineering. Designers have version history in Figma, writers use tracked changes, and everybody has saved a deck as v1, v2, v3. One question underneath all of it: I want to change this without wrecking what already works. One answer: copy it, work on the copy, swap it in.
>
> Next time you move to a different deployment platform, use the pattern as a checklist. What does it call the isolated space, and which action counts as merging to the main line? Answer those two and you're basically productive.
>
> Where it comes from: [section 11 of 04-deployment-environment-and-git-branch, "Mentor's Note"](../04-deployment-environment-and-git-branch/README.md).