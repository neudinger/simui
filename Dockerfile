FROM scratch

COPY ./dist/simui_static /simui_static

ENTRYPOINT ["/simui_static"]
CMD [""]