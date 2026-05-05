FROM manimcommunity/manim:latest
WORKDIR /app
COPY . .
ENTRYPOINT ["manim"]
