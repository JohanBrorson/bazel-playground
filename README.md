# bazel-playground

## Running

```shell
bazel run //app:calculator
```

## Testing

```shell
bazel test //...
```

### Formatting

**Note!** Formatting currently only works for BUILD and Markdown files.

```shell
bazel run @aspect_rules_format//format
```
