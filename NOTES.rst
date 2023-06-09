Title Page
-----------

I'm Tom Rothamel, and this is my talk on Making Visual Novels with Ren'Py.
Before we begin, a little about me. I'm the creator and lead developer of
the Ren'Py visual novel engine. I've been working on Ren'Py since 2004.

I'm also a Stony Brook alumni, twice over - 2001 and 2008, and back in
the day I was a volunteer at I-CON, the last con held at Stony Brook -
one year, I ran a video room that showed Cowboy Beybop and Captain Tylor.


Agenda
------

Let's talk about what's on the agenda for today's talk.

First off, I'm going to start off with my idea of what a visual novel is,
a quick history of visual novels, and why I think they're important.

Then I'll be talking about the Ren'Py engine - what is, where it runs,
and who it's for.

After that, I'll be in the main part of the talk, a quick introduction to
how to make games with Ren'Py. Today I'm going to cover the higlights of
how to make a visual novel.

Finally, at the end I'll answer any questions you might have.


What are Visual Novels?
-----------------------

(Click through.)

Visual novels are a type of digital storytelling that uses text, images,
sound and more.

In my opinion, storytelling is what separates a visual novel from other
kinds of games. If the story is the predominant reason to play a game,
it's a visual novel. Compare that to games with rewarding gameplay, or
ones are experiences.

Many visual novels have a shared experience, and we're seing some of it
right now. We have a background image, that shows where we are, and a
text box - since there's no name there, this is narration.

(Click.)

We clicked through, and clicking advances the story. A sprite showed up,
which conveys characrer and emotion. The text box changes, and now it has
a name, so this is dialogue - Eileen is speaking to us.

(Click.)

What we have here is a menu. It has a caption - Eileen is asking us a
question. We can make a choice, and that controls what happens next.

(Make either choice.)

History of VNs.
---------------

Let me start off by saying that I'm not an expert on what happened in Japan,
and while I've been part of the English language community, this is just
what I've pierced together.

One of the first adventure games was ADVENT, or Collossal Cave Adventure,
released in 1976. It's a text base game, you enter in simple commands.
Take keys, light lamp, etc.

This formed a genre - Zork is famous, but there were many othere. It looks like
it went to Japan.

(Portopia Serial Murder Case)

This was released for computers in Japan in 1983, and it was a text adventure
with pictures. It was released for the Famicom for the NES. This is the box
art...

(click)

... the game looks like this. Not bad when you realize that the entire game
was 40 kilobytes - smaller than the picture. You can sort of see the basics
of the VN here - instead of text, you pick off a menu.

(To Heart)

The term Visual Novel comes from Leaf's Visual Novel series, from the mid
1990s. This is To Heart from 1996. At least for a long time, Visual Novel
was a trademark of Leaf, used for their games, with Novel games being
the generic.

To Heart has a lot of hallmarks of what visual novels have become.

(Kanon)

In addition to Kanon, which came out in 1999. This probably would still
be called an adventure game in Japan, as it uses a partial screen textbox
but between the two of these, we see the basic elements of modern vns
have developed.

Both To Heart and Kanon had anime in the 2000s, which seeded the English-language
VN community.

(Ever 17)

In addition, we started getting translated games coming over to the US. This
is Ever 17 - released in Japan in 2002 and the US in 2005, right as the
VN community was starting.

(Tales of Lemma)

Stepping back, we cna see one of the earliest English-language VNs, Tales of
Lemma 1. It was released in 2003, and shows much of the same elements as
a modern VN. The Lemma Soft Forums formed around it. They're still around
and are responsible for much of the English-language VN community.

Lemma called the games Ren'Ai games - romantic games - the Visual Novel term
wasn't developed yet. That's where the Ren in Ren'Py games from.

(Katawa Shoujo)

Under devlopment from 2004 to 2013, and it helped to grow the English-language
community, and inspire other developer. That kind of leads a cycle where
people become inspired, some make their own game, and then:

(DDLC)

They make a game that inspires others, like Doki Doki Literature club, from 2017
and  the cycle continues.


Why Visual Novels
------------------

I tend to think one of the big appeals of Visual Novels is that they're
a medium that's both first person and visual. There's an immediacy that
you don't get in a novel or even light novels - visual novels are constantly
using multiple types of media to tell a story

At the same time, the story can get into character's heads more than comics
and movies can - you can see what they're thinking and feeling. That's hard
to do in movies, and in comics - you'd have to draw a new panel for every
thought.

Another thing I like is that Visual Novels can be made by small teams, which
means you're getting a single creator's vision. Often times, one person can
write, draw, and program a visual novel. Sometimes those functions are
separate people, or multiple people - and often times, there will be
other roles - musicians, voice actors, proofreaders, etc.

But the point is that many visual novels are made by a small team, and so
you're getting that small team's vision - what's important to them is on the
screen. That makes visual novels a good visual medium for people that might
not be otherwise represented.

And it brings me to the motivation for Ren'Py. Before Ren'Py, each team that
wanted to make a visual novel had to write their own engine. That requires
a decent of programming skill to pull off, and so it was a barrier to entry.
The motivation behind Ren'Py was to remove that barrier.

And so, 19 years later, we make it to our next section.

What is Ren'Py
--------------

Ren'Py is a free and open source visual novel engine. It's been around since
2004. It's free to download, free to use, and you can distribute the games
you make with it for free. It's also open source, so you can look at how
it works, and you can modify it to do what you want - though I'd perfer
you contribute your changes back to the project.

Ren'Py is written in Python, which is a programming language that's easy to
learn, though part of the motivation for it is that you can make a basic
visual novel without knowing Python.

Ren'Py runs on Windows, Mac, Linux, Android, iOS, and Chromebook. It runs
in web browsers. It's not supported by the Ren'Py team, but a company has
taken the code and made a version that runs on the Nintendo Switch, Playstation,
and Xbox.

Ren'Py is Meant For
-------------------

Ren'Py is mainly meant for visual novels, and other choice based games.

It does well in life simulation games - that's genre where you make choices
at the start of a day to affect how your day goes, and the game will run
you through them, simulating encounters and telling story.

It's also being used for choice-based RPGs, like Magical Diary: Wolf Hall
here. I'm focusing on visual novels today, but this gives you an idea of
what's possible.

Ren'Py, though, is not meant for all games. It's not meant for arcage games,
or anything else that requires real time input. It can't do online games.
The goal is to focus on visual novels, and to do them well - and if you'd
like another genre, there are plenty of other engines.


Ren'Py is Meant For
-------------------

Let's talk about who Ren'Py is meant for.

It's meant for experience programmers. The Py and Ren'Py is for Python,
and one nice thing about Ren'Py is that you can replace a lot of it with
your own Python code, to totally customize your game.

It's also meant for intermediate programmers. If you know a little bit of
Python, you'll be able to leverage that to provide logic for your game.

And it's meant for non-programmers. You don't need to know how to program,
to get started using Ren'Py. You can make a basic visual novel without
knowing how to program - though you're not going to make Wolf Hall.

Our goal is to make it accessible to all creators, and easy to learn, at
least to make a basic visual novel. We don't shy away from programming -
our goal is to make it something everyone can do.

Thousands of Games Have Been Made With Ren'Py
---------------------------------------------

And we've done that. Thousands of games have been made with Ren'Py,
1,650 Ren'Py games were released in 2022 - you're seeing a small
fraction of them right now.

Over 1,700 of those games are on Steam - Ren'Py is the 5th most used
engine on Steam.

We're keeping up work on Ren'Py - Ren'Py 8.1 is going to be great. And
I look forward to seeing what you make with it - so let's talk about...


How do I make A Visual Novel With Ren'Py
-----------------------------------------

First off, let me just say that I'm going to focus on the Ren'Py part of
how to make a visual novel with Ren'Py. There are lots of other skills
that you'll need to make a visual novel - writing, drawing, music, etc, and
I'm going to just assume you already have them.

If you want a more wholistic view of what's important - check out visual;conference.
It's a conference for visual novel creators, and you can find videos of it
on YouTube.

Download and Install Ren'Py.
----------------------------

You should be able to download and install Ren'Py from the website. If you're
making an new game, get Ren'Py 8 - it's the latest version, while Ren'Py
7 is for legacy games. How you download it and run it depends on your
platform, but once you have it.

(Launch the launcher.)

You'll see the Ren'Py launcher. The first time you run it, it'll ask you
your language, and where you want your projects to go. From it, you can
pick the Tutorial, or the sample game, The Question. And then if you click
launch, it'll run the game for you.

We're not going to do that. We're goig to make a new game - click here. It's
telling us we're making a project in English, Continue, and then we enter the name.

"brookcon"  <enter>

It's asking how big we want the game - full hd is a good choice if you
don't know you want bigger.

And it's aksing for your interface colors. The dark colors work a bit better,
so we'll click green.  And it's making the project and getting it ready for
us.

We can edit the project - but we have an example project ready, so I'll switch
to that.

We can click on the directories to open them - images can go into the images
directory, audio goes into the audio directory, and everything else goes into
game. On the right, you can click a file to open it in an editor - if you
don't have an editor, Ren'Py will get one. I recommend Visual Studio Code.

And on the bottom here are a number of buttons to help you navigate your
game, and to run it.

(Show them the game.)

Before we switch back, let me just show you a few things. This is a brand
new game, but we have features people expect, like loading and saving, history,
and rollback.

There is a set of preferences to let people control the speed of the text,
volumes, auto-forward, and more.

And there are even some acessibility features. If we hit v, the game will
read text to us. And if we hit shift+A, there are a number of options to
make the game easier to read.


Our First Script
----------------

Here's the script for what you just saw. Apart from adding in image files,
this is everything I wrote.

Let's break it dow, bit by bit.

Dialogue
--------

Narraiton and Dialogue are at the heart of most visual novels, so I've tried
to make them easy to write. Narration is just in quotes, and dialogue has a
short name in front of it - the short name is there so you don't have to
constantly retype it.

The define statement at the start of the file is defining the short name, in
this case, Eileen. We define it to be a character, and we give it a name. If you
wanted to customize it more, you could do that here.

You'll do the define once, while narration and dialogue happen many many
times during the game.

Image Names
-----------

Before we show an image, it helpe to know how Ren'Py defines and names images.
To define an image, put it in the images directory. Start it with a letter,
and avoid special characters. Ren'Py will force the name to be lowercase,
and split it up into a tag and attributes in spaces.

The first part of the image is the tag. Every image has to have a tag.
The rest are the attributes - you can have as many as you want, or none
at all.

So, for eileen happy.jpg, the image name is eileen happy, the tag is eileen
and the attribute is happy. This is important because you can only have one
image wih the same tag on the screen at a time - if you show another image
with the same tag, it replaces the first.

All names (tags, attributes, labels, etc) have to start with a letter,
and can contain letters, numbers, and underscores. They can't contain
other special characters.

Scene, Show, and Hide
----------------------

How do we show an image - there are two ways. The first is to use the scene
statement, which hides everything else that's showing, and then shows an
image. This is really useful when the game changes location - you'd want
everything at the first location to go away, and start with a blank
slate.

The show statement shows an image. If an image with the same tag is already
shown, it replaces it. So you'd use show the first time a sprite shows up,
and then again to change to change the emotions displayed.

Finally the hide statement hides an image. You don't use it that much, only
when a sprite leaves while keeping the scene the same.


Label, Jump, and Return
-----------------------

The label statement defines a label, which is a place in the script with
a name. You usually indent the things under the label by 4 spaces - it makes
it easy to scan the file and see what's under a label.

The jump statement jumps to a label. It's a way to jump around in the game.
Ren'Py will load in all files ending with .rpy, so you can jump to a label
in a different file. That's how you spit a game up over multiple files.

There's a call statement, which we're not covering today, and a return statement
which we are. If we reach a return statement without a call, we go to the
main menu.


Choice Menus
------------

A big part of visual novels is the choice menu. The menu statment defines
a choice menu. You start off with menu, and a colon, and then everything
is indented by four spaces.

Next up is the caption, prompting the user. That's dialogue, but it can also
be narration, or just left out.

You then have the choices, which are in quotes - a string - and ending with
a colon. What's under that is what's run when the choice is picked. In this case,
both choices cause a jump to happen.

Always indent with four spaces - everything will line up, and your life will
be eaiser. Visual Studio Code should do that automatically for you, most of
the time.

This is just about it - everything you saw in the example game, except for
some of the polish. But polish is nice, so let's start with:


Playing Music
-------------

Fairly simple, play music and the name of the file to play, in the audio
directory. A second play music statement will replace what's currently playing.

You can also use the stop music statement to stop the music.


Transforms
----------

Transforms change what's being shown, and the most common use of them in
simple visual novels is to change the location of a sprite. You introduce
the transform by adding 'at' to the show statement, and then giving the
transform.

Here, we're using right, so Eileen is showing on the right side of the screen,
you can also give left and center.

Custom Transforms
------------------

You can also define your own transform. Just put the transform statement
at the start of a file, and then put align right after it. You give it
X and Y, with X going from left to right, and Y from top to bottom. You
always want to give it the decimal - write 1.0 rather than 1.

You can then use it just like the built-in transforms. In fact - the builtin
transforms are just custom transforms defined by Ren'Py. That's part of
the way Ren'Py works - we provide a few simple ways to things, and give
you the way to do it yourself.

Transitions
-----------

If you saw before, when Eileen moved, it was very abrupt - she'd just pop
in and out. Transitions are a way to make that smoother. You introduce
a transition by writing 'with' after the show statement, and then giving
the transition to use.

With dissolve will smoothly blend from old to new.

(click)

With fade will take the screen to black, and then bring it back. This is a
good one to use when changing from scene to scene.

(click)

There are a lot of transitions, and you can define your own to change the timing,
but dissolve is probably the most used.

Python
------

We've gotten this far without any Python. That's not totally true - when
we defined the e Character, that was Python, just a little bit of it. Ditto
when we gave the position of the transition.

A little bit more Python can make the game a bit more interactive.

The default statment sets the default value of a variable. In this case, we'll
default the player's score to 0 when the game starts.

The Python statement is how we can invoke abitrary games, but basic visual
novels tend to use simple  python. Score equals score plus 1 is how we
increase the score by one when the player makes a choice we want to
reward.

Finally, we can use the if statement to make a decision. Here, we'll say
if the score is greater than 3 - four or more - we'll go to the good end.
Otherwise, we'll give the player a bad end.

Advanced Python programmers can do a lot with Ren'Py. But you don't need a
lot to be useful, and many games can do nothing at all.

Example
-------

And just to show that, here's a section of The Question, the game that
comes with Ren'Py as an example - the quickstart section of the documentation
walks you through making it.

I'm showing you this because I think I told you a lot of things, but you'll
only use a few of them, most of the time. See the lines in green? Those are
narration and dialogue - and that's most of the game.

You'll also see some show and scene statements, and they tend to have
a with statement. At the top there's a label, and at the bottom a menu
with a couple of jumps.

That's it.

When you're making visual novels, you don't need a lot of complexity - and
you should start by making something simple, and then expanding.

What We Didn't Cover
--------------------

There's a lot of stuff we didn't cover in this, so this talk didn't get too
complicated.

Ren'Py supports playing back movies - especially webm movies - if you need
it to.

It supports voice acting, and there are a lot of voice acted games.

There's a full translation system, so you can send templates to a
translation team, and Ren'Py will stick those into the game.

ATL. I showd you a basic transform, but ATL - the animation and transform
language - is it's own thing, and you can do all sorts of animations and
movments with it.

There's a gui system - you can get to it by clicking gui in the launcher.
You can customize Ren'Py by changing the pictures there, and the numbers
and colors in gui.rpy. All the changes between the example game and
these slides were done with the gui system.

Screen Language is used for more complicated customizations - replacing
the gui, and can also be used for your own game to interact with the player.

And finally, Ren'Py is written in Python, and as much as possible, you
can make your own extensions to it in Python.


For More Information
--------------------

The documentation is on the Ren'Py website, and there's a lot of information
there. You can also ask questions on the Ren'Py Discord server, or go from
there to the Lemma Soft forums.

You have an option most people don't have! Stony brook has a great game design
and development club, and they've been running a Ren'Py jam for 5 years now.
It just finished, seven games were made, and I'm sure there are a lot of people
there with Ren'Py skill. I thin some of them might be better at Ren'Py than I am.

Thank You
---------

And that's it!

Let me just say thank you - to GDDC for bringing me here, to the Brook Con
organizers for bringing a con back to Stony Brook, and to you for coming
here. No pressure, but I look forward to seeing what you make.

And with that - any questions?
